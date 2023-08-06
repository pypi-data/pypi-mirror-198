"""Cavnar Trenkle implementation module."""

from __future__ import division # Safety measure in case we extend to py2.7

from collections import defaultdict
import sys

from nltk.tokenize import wordpunct_tokenize
from nltk.util import ngrams

from pylade import utils
from .implementation import Implementation


# TODO: Store instance variables (e.g. model)
class CavnarTrenkleImpl(Implementation):
    """Cavnar Trenkle implementation class."""

    def train(self, labeled_instances, limit=None, verbose=False):
        """Train the model.

        Args:
            labeled_instances (iterable): An iterable whose elements are
                dictionaries. These dictionaries must have `text` and `language`
                keys with their relative values.
            limit (int): The number of entries in the training language
                profiles. Less entries make training faster, but it is better
                to keep a balance between speed and accuracy.
            verbose (bool): If `True`, print information about training.

        Returns:
            A list of language profiles.

            A profile is a list of ngrams sorted in reverse order (from the
            most frequent to the less frequent). Each language has its own list
            (profile). This method returns a dictionary in which each key is a
            language whose value is a list of ngrams (the language profile).

        """
        if verbose:
            print("Training. Limit: {}".format(limit))

        language_profiles = dict()
        languages_ngram_freqs = self._languages_ngram_frequencies(labeled_instances)
        print("Sorting language profiles in lists")
        for language in languages_ngram_freqs:
            language_profiles[language] = self._compute_profile_from_frequencies(
                languages_ngram_freqs[language], limit)
        return language_profiles

    # TODO: model should be an instance variable. Actually, the implementation
    # IS the model
    def evaluate(self, model, test_instances, languages=None, error_values=None,
                 split_languages=False):
        """Evaluate model on test data and gather results.

        Args:
            model: A list of training profiles for languages.
            test_instances (iterable): An iterable whose elements are
                dictionaries. These dictionaries must have `text` and `language`
                keys with their relative values.
            languages (iterable): A list of language labels. When specified,
                the model is  only evaluated on test instances with these labels
                (e.g. 'it').
            split_languages (bool): if `True`, each language in `languages` is
                evaluated separately and results will be split by language. If
                `False` (default) results are computed over all instances
                belonging to `languages`.

        Yields:
            A single result in the form of `{'tested_languages': {error_value:
            accuracy}}`

        NOTE:
            If you want to use `test_instances` multiple times, they need to be
            stored in a list. Since they are a generator object, they would be
            exhausted after the first iteration.

        """
        if error_values is None:
            error_values = [8000]

        # Make sure it is a list of integers:
        if isinstance(error_values, (int, float, str)):
            error_values = [int(val) for val in [error_values]]

        # Make sure that test_instances is a list when we need multiple iterations
        if len(error_values) > 1 or split_languages is True:
            test_instances = list(test_instances)

        print("Evaluating...")

        if languages and split_languages is True:
            # Evaluate performance on each language separately
            for lang in languages:
                yield from self._eval_single_result(
                    error_values, test_instances, model, [lang])
        else:
            # Evaluate performance on all (specified) languages together
            yield from self._eval_single_result(
                error_values, test_instances, model, languages)

    def predict_language(self, text, training_profiles, error_value=8000):
        """Predict language for a text.

        Args:
            text (str): A text whose language has to be detected.
            training_profiles (dict): A dictionary whose keys are language
                labels. Each value is a list of 'ngrams' sorted by frequency.
                This is the actual model used for prediction.
            error_value (int): The amount that penalizes the prediction whenever
                an ngram is not present in the training profile. This value
                should be decided based on tuning on the test set. See paper for
                more details.

        Returns:
            The predicted language label (e.g. 'en').

        >>> implementation = CavnarTrenkleImpl()
        >>> text = 'hello'
        >>> training_profiles = {
        ... 'en': ['l', 'o', 'lo', 'llo', 'll', 'hello', 'hell', 'hel', 'he',
        ...       'h', 'ello', 'ell', 'el', 'e'],
        ... 'it': ['o', 'iao', 'ia', 'i', 'ciao', 'cia', 'ci', 'c', 'ao', 'a']}
        >>> implementation.predict_language(text, training_profiles)
        'en'

        NOTE:
            This is the same as:

            >>> lang_distances = self.predict_language_scores( # doctest: +SKIP
            ...    text, training_profiles, error_value)
            >>> min(lang_distances, key=lang_distances.get) # doctest: +SKIP

        NOTE:
            This method could be improved by simply iterating over distances and
            discarding them when they are smaller than the previous one. This
            would not allow us to reuse `predict_language_scores` here.

        """
        min_distance = sys.maxsize # Set it to a high number before iterating
        predicted_language = ''
        text_profile = self._compute_text_profile(text)

        for language in training_profiles:
            distance = self._distance(
                text_profile, training_profiles[language], error_value=error_value)
            if distance < min_distance:
                min_distance = distance
                predicted_language = language

        return predicted_language

    # Private methods #

    def _compute_profile_from_frequencies(self, frequencies_dict, limit):
        # Sort by value first, and then also by key (alphabetic order) if values
        # are equal.
        return [ngram[0] for ngram in sorted(
            frequencies_dict.items(),
            key=lambda x: (x[1], x[0]),
            reverse=True)[:limit]]

    def _compute_text_profile(self, text, limit=None):
        """
        >>> implementation = CavnarTrenkleImpl()
        >>> text = 'Hello'
        >>> implementation._compute_text_profile(text) # doctest: +NORMALIZE_WHITESPACE
        ['l', 'o', 'lo', 'llo', 'll', 'hello', 'hell', 'hel', 'he', 'h',
        'ello', 'ell', 'el', 'e']
        >>> implementation._compute_text_profile(text, limit=2)
        ['l', 'o']

        """
        text_ngram_freqs = self._extract_text_ngram_freqs(text)
        return self._compute_profile_from_frequencies(text_ngram_freqs, limit)

    def _distance(self, text_profile, training_profile, error_value=1000):
        """Compute the distance between two profiles.

        This method compares two profiles and returns a number which represents
        the distance between them. A high distance means that the language of
        the texts that have been used to generate the profiles is not the same.
        This distance is called "out-of-place" metric in the paper.
        We usually compare a language profile (generated from a training set)
        to the profile generated from a single text (e.g. a tweet or a facebook
        post).
        Note: If a ngram is not present in the training profile, we penalize
        the text profile using an arbitrary `error_value`. This value should
        be decided based on tuning on the test set.

        >>> text_profile = ['h', 'e', 'l', 'o', 'he']
        >>> training_profile = ['h', 'e', 'l', 'o', 'he']
        >>> implementation = CavnarTrenkleImpl()
        >>> implementation._distance(text_profile, training_profile)
        0
        >>> training_profile = ['l', 'o', 'h', 'e', 'he']
        >>> implementation._distance(text_profile, training_profile)
        8

        """
        total_distance = 0
        for index, text_ngram in enumerate(text_profile):
            if text_ngram in training_profile:
                distance = abs(index - training_profile.index(text_ngram))
            else:
                distance = error_value
            total_distance += distance

        return total_distance

    def _evaluate_for_languages(self, test_instances, model, error_value,
                                languages=None):
        correct = 0
        incorrect = 0
        total = 0
        for labeled_instance in test_instances:
            # Skip instances with different languages
            # TODO: This would not be necessary if we could use only instances
            # with specific labels (a subset of test_instances). To be fixed.
            if languages and labeled_instance['language'] not in languages:
                continue
            predicted_language = self.predict_language(
                labeled_instance['text'], model, error_value=error_value)
            if predicted_language == labeled_instance['language']:
                correct += 1
            else:
                incorrect += 1
            total += 1

            print(
                "Label: {}, Guess: {}, Correct: {}, Incorrect: {}, Total: {}   ".format(
                    labeled_instance['language'],
                    predicted_language,
                    correct,
                    incorrect,
                    total),
                end='\r', flush=True)
        print()
        accuracy = correct / total
        # single_result = {languages: {str(err_val): accuracy}}
        # TODO: this should be a dictionary: {'accuracy': accuracy}
        return accuracy

    def _eval_single_result(self, error_values, test_instances, model, languages=None):
        """Evaluate performance on specified languages.

        If no languages have been specified, use all available languages.

        """
        tested_langs = ' '.join(languages) if languages else 'ALL'
        for err_val in error_values:
            print("Evaluating results for LANG: {}, ERR_VAL: {}".format(
                tested_langs,
                err_val))
            accuracy = self._evaluate_for_languages(
                test_instances, model, err_val, languages)
            single_result = {tested_langs: {str(err_val): accuracy}}
            yield single_result

    def _extract_text_ngram_freqs(self, text):
        """Tokenize the text.

        For each token in the text, extract ngrams of different length (from 1
        to 5). Compute how many times each of these ngrams occur in the text.
        Then return a dictionary of { ngram: frequencies }.

        >>> implementation = CavnarTrenkleImpl()
        >>> ngrams = implementation._extract_text_ngram_freqs("HeLLo")
        >>> ngrams == {'h':1, 'e': 1, 'l': 2, 'o': 1, 'he': 1, 'el': 1, 'll': 1, \
            'lo': 1, 'hel': 1, 'ell': 1, 'llo': 1, 'hell': 1, 'ello': 1, 'hello': 1}
        True
        >>> ngrams = implementation._extract_text_ngram_freqs("CIAO")
        >>> ngrams == {'c':1, 'i': 1, 'a': 1, 'o': 1, 'ci': 1, 'ia': 1, 'ao': 1, \
            'cia': 1, 'iao': 1, 'ciao': 1}
        True

        """
        tokens = wordpunct_tokenize(text.lower()) # Force lower case
        # TODO: Delete numbers and punctuation
        # TODO: Should we use nltk twitter tokenizer?

        ngram_freqs = defaultdict(int)
        for token in tokens:
            for n in range(1, 6): # Use 1-grams to 5-grams
                for ngram in ngrams(token, n):
                    ngram_string = ''.join(ngram)
                    ngram_freqs[ngram_string] += 1
                # ngram_freqs[ngrams(token, n)] += 1

        return ngram_freqs

    def _languages_ngram_frequencies(self, labeled_instances):
        """Compute ngram frequencies for each language in the corpus.

        >>> implementation = CavnarTrenkleImpl()
        >>> tweets = [{'language': 'it', 'id_str': '12', 'text': 'Ciao'}, \
                      {'language': 'en', 'id_str': '15', 'text': 'Hello'}]
        >>> lang_ngram_freqs = implementation._languages_ngram_frequencies(tweets)
        >>> lang_ngram_freqs == {\
            'it': {'c':1, 'i': 1, 'a': 1, 'o': 1, 'ci': 1, 'ia': 1, 'ao': 1, \
                   'cia': 1, 'iao': 1, 'ciao': 1}, \
            'en': {'h':1, 'e': 1, 'l': 2, 'o': 1, 'he': 1, 'el': 1, 'll': 1, \
                   'lo': 1, 'hel': 1, 'ell': 1, 'llo': 1, 'hell': 1, 'ello': 1, \
                   'hello': 1}}
        True

        """
        # freqs = defaultdict(lambda : defaultdict(int)) # Not working with Pickle
        freqs = defaultdict(utils.nested_defaultdict)
        for instance in labeled_instances:
            lang = instance['language']
            instance_ngram_freqs = self._extract_text_ngram_freqs(instance['text'])
            utils.merge_dictionaries_summing(freqs[lang], instance_ngram_freqs)

        return freqs
