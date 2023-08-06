# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['llamacpp']

package_data = \
{'': ['*']}

install_requires = \
['sentencepiece>=0.1.97,<0.2.0', 'torch>=1.13.1,<2.0.0']

entry_points = \
{'console_scripts': ['llamacpp-chat = llamacpp.chat:run',
                     'llamacpp-cli = llamacpp.cli:run',
                     'llamacpp-convert = llamacpp.convert:main',
                     'llamacpp-quantize = llamacpp.quantize:main']}

setup_kwargs = {
    'name': 'llamacpp',
    'version': '0.1.5',
    'description': "Python bindings for @ggerganov's llama.cpp",
    'long_description': '## Python bindings for llama.cpp\n\n## Building the Python bindings\n\n### macOS\n\n```\nbrew install pybind11  # Installs dependency\ngit submodule init && git submodule update\npoetry install\n```\n### From PyPI\n\n```\npip install llamacpp\n```\n\n## Get the model weights\n\nYou will need to obtain the weights for LLaMA yourself. There are a few torrents floating around as well as some huggingface repositories (e.g https://huggingface.co/nyanko7/LLaMA-7B/). Once you have them, copy them into the models folder.\n\n```\nls ./models\n65B 30B 13B 7B tokenizer_checklist.chk tokenizer.model\n```\n\nConvert the weights to GGML format using `llamacpp-convert`. Then use `llamacpp-quantize` to quantize them into INT4. For example, for the 7B parameter model, run\n\n```\nllamacpp-convert ./models/7B/ 1\nllamacpp-quantize ./models/7B/\nllamacpp-cli\n```\n\n## Command line interface\n\nThe package installs the command line entry point `llamacpp-cli` that points to `llamacpp/cli.py` and should provide about the same functionality as the `main` program in the original C++ repository. There is also an experimental `llamacpp-chat` that is supposed to bring up a chat interface but this is not working correctly yet.\n\n## Demo script\n\nSee `llamacpp/cli.py` for a detailed example. The simplest demo would be something like the following:\n\n## ToDo\n\n- [x] Use poetry to build package\n- [x] Add command line entry point for quantize script\n- [x] Publish wheel to PyPI\n- [ ] Add chat interface based on tinygrad\n',
    'author': 'Thomas Antony',
    'author_email': 'mail@thomasantony.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/thomasantony/llamacpp-python',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
