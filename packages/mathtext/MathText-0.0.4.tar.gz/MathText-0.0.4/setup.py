# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mathtext']

package_data = \
{'': ['*'], 'mathtext': ['data/*']}

install_requires = \
['editdistance',
 'gradio>=3.14.0,<3.15.0',
 'httpx>=0.23.0,<0.24.0',
 'jupyter',
 'matplotlib>=3.5.0,<3.6.0',
 'pandas-gbq>=0.19,<0.20',
 'pandas>=1.3,<2.0',
 'pytest>=7.2.0,<7.3.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'scikit-image',
 'scikit-learn>=1.0,<2.0',
 'spacy>=3.4,<4.0',
 'torch>=1.12,<2.0',
 'transformers>=4.24,<5.0']

setup_kwargs = {
    'name': 'mathtext',
    'version': '0.0.4',
    'description': 'Natural Language Understanding (text processing) for math symbols, digits, and words with a Gradio user interface and REST API.',
    'long_description': "---\ntitle: MathText\napp_file: app.py\nsdk: gradio\nsdk_version: 3.15.0\nlicense: agpl-3.0\n---\n\n## MathText NLU\n\nNatural Language Understanding for math symbols, digits, and words with a Gradio user interface and REST API.\n\n## Setup your Python environment\n\nLaunch a `terminal` on linux (or the `git-bash` application on Windows).\nThen create a virtualenv with whatever python version you have available on your system.\n\nAny python version greater than `3.7` should work.\nMost of us on Linux systems use Python `3.9`: \n\n```bash\ngit clone git@gitlab.com:tangibleai/community/mathtext\ncd mathtext\npip install --upgrade virtualenv poetry\npython -m virtualenv --python 3.9 .venv\nls -hal\n```\n\nYou should see a new `.venv/` directory.\nIt will contain your python interpreter and a few `site-packages` like `pip` and `distutils`.\n\nNow activate your new virtual environment by sourcing `.venv/bin/activate` (on Linux) or `.venv/scripts/activate` (on Windows).\n\n```bash\nsource .venv/bin/activate || source .venv/scripts/activate\n```\n\n## Developer installation\n\nOnce you have a shiny new virtual environment activated you can install the `mathtext` in `--editable` mode.\nThis way, when you edit the files and have the package change immediately.\n\nMake sure you are already within your cloned `mathtext` project directory.\nAnd makes sure your virtual environment is activated.\nYou should see the name of your virtual environment in parentheses within your command line prompt, like `(.venv) $`.\nThen when you install MathText it will be available to any other application within that environment.\n\n```bash\npip install --editable .\n```\n\n## User installation\n\nIf you don't want to contribute to the MathText source code and you just want to import and run the MathText modules, you can install it from a binary wheel on PyPi.\n\n```bash\npip install mathtext\n```\n\n\n\n## File notes\n    mathtext\n        mathtext: mathtext code\n            data: training and test sets for various tasks\n            api_gradio.py: gradio api\n            api_scaling.py: makes async http requests to the local api\n            nlutils_vish.py: various NLP utils\n            nlutils.py: various NLP utils\n            plot_calls.py: Functions for plotting data\n            readme.md: other readme?\n            sentiment.py: sets up huggingface sentiment analysis pipeline for the api (gradio or FastAPI?)\n            tag_numbers.py: Number and word POS tagger\n            text2int.py: text2int function\n        scripts: setup scripts\n            build.sh\n            pyproject.template\n        tests: various tests\n            __init.py\n            test_text2int.py\n        .git*: various git files\n        api_scaling.sh: makes calls to local api\n        app.py: ties all of the api components together for huggingface\n        LICENSE.md: license\n        pyproject.toml: pyproject file\n        README.md: this\n        requirements.txt: project dependencies\n            ",
    'author': 'Sebastian Larson',
    'author_email': 'sebastianlarson22@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
