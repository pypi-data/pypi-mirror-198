# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylade',
 'pylade.console_scripts',
 'pylade.console_scripts.args_parsers',
 'pylade.corpus_readers',
 'pylade.implementations']

package_data = \
{'': ['*'], 'pylade': ['data/*']}

install_requires = \
['nltk>=3.8.1,<4.0.0']

entry_points = \
{'console_scripts': ['pylade = pylade.console_scripts.detect:main',
                     'pylade_eval = pylade.console_scripts.evaluate:main',
                     'pylade_train = pylade.console_scripts.train:main']}

setup_kwargs = {
    'name': 'pylade',
    'version': '0.2.1',
    'description': 'PyLaDe - Language Detection tool written in Python.',
    'long_description': '# PyLaDe\n\n[![Build Status](https://travis-ci.org/fievelk/pylade.svg?branch=master)](https://travis-ci.org/fievelk/pylade)\n\n`pylade` is a lightweight language detection tool written in Python. The tool provides a ready-to-use command-line interface, along with more complex scaffolding for customized tasks.\n\nThe current version of `pylade` implements the *Cavnar-Trenkle N-Gram-based approach*. However, the tool can be further expanded with customized language identification implementations.\n\n- [Installation](#installation)\n- [Usage](#usage)\n  - [Train a model on a training set](#train-a-model-on-a-training-set)\n  - [Evaluate a model on a test set](#evaluate-a-model-on-a-test-set)\n  - [Detect language of a text using a trained model](#detect-language-of-a-text-using-a-trained-model)\n  - [Custom implementations and corpora](#custom-implementations-and-corpora)\n- [Development and testing](#development-and-testing)\n- [Notes](#notes)\n- [References](#references)\n\n\n## Installation\n\nYou can install using pip:\n\n```bash\n$ pip install pylade\n```\n\n\n## Usage\n\nFor a quick use, simply give the following command from terminal:\n\n```console\n$ pylade "Put text here"\nen\n```\nDone!\n\nIf you want to get deeper and use some more advanced features, please keep reading. **Note:** you can obtain more information about each of the following commands using the `--help` flag.\n\n### Train a model on a training set\n\n```console\n$ pylade_train \\\n    training_set.csv \\\n    --implementation CavnarTrenkleImpl \\\n    --corpus-reader TwitterCorpusReader \\\n    --output model.json \\\n    --train-args \'{"limit": 5000, "verbose": "True"}\'\n```\n\n`--train-args` is a dictionary of arguments to be passed to the `train()` method of the chosen implementation (`CavnarTrenkleImpl` in the example above). For an accurate description of the arguments please refer to the `train()` method docstring.\n\n**NOTE**: to define a new training set, you can check the format of the file `tests/test_files/training_set_example.csv`.\n\n### Evaluate a model on a test set\n\n```console\n$ pylade_eval \\\n    test_set.csv \\\n    --model model.json \\\n    --implementation CavnarTrenkleImpl \\\n    --corpus-reader TwitterCorpusReader \\\n    --output results.json \\\n    --eval-args \'{"languages": ["it", "de"], "error_values": 8000}\'\n```\n\n`--eval-args` is a dictionary of arguments to be passed to the `evaluate()` method of the chosen implementation (`CavnarTrenkleImpl` in the example above). For an accurate description of the arguments please refer to the `evaluate()` method docstring.\n\n### Detect language of a text using a trained model\n\n```console\n$ pylade \\\n    "Put text here" \\\n    --model model.json \\\n    --implementation CavnarTrenkleImpl \\\n    --output detected_language.txt \\\n    --predict-args \'{"error_value": 8000}\'\n```\n\n`--predict-args` is a dictionary of arguments to be passed to the `predict_language()` method of the chosen implementation (`CavnarTrenkleImpl` in the example above). For an accurate description of the arguments please refer to the `predict_language()` method docstring.\n\n### Custom implementations and corpora\n\nDifferent language detection approaches can be implemented creating new classes that inherit from the `Implementation` class. This class should be considered as an interface whose methods are meant to be implemented by the inheriting class.\n\nCustomized corpus readers can be created the same way, inheriting from the `CorpusReader` interface instead.\n\n\n## Development and testing\n\nYou can install development requirements using Poetry (`poetry install`). This will also install requirements needed for testing.\n\nTo run tests, just run `tox` from the package root folder.\n\n\n## Notes\n\nThe default model (`data/model.json`) has been trained using `limit = 5000`. This value provides a good balance between computational performance and accuracy. Please note that this might change if you use your own data to train a new model.\n\n\n## References\n\n- Cavnar, William B., and John M. Trenkle. "N-gram-based text categorization." *Ann Arbor MI* 48113.2 (1994): 161-175.\n',
    'author': 'Pierpaolo Pantone',
    'author_email': '24alsecondo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/fievelk/pylade',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<=3.12',
}


setup(**setup_kwargs)
