# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exhbma']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0',
 'numpy>=1.22.1,<2.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'scipy>=1.7.3,<2.0.0',
 'tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'exhbma',
    'version': '0.1.12',
    'description': 'Exhaustive Search with Bayesian Model Averaging',
    'long_description': '# Exhaustive Search with Bayesian Model Averaging (ExhBMA)\n\n# Installation\n```\npip install exhbma\n```\n\n# Documentation\nUser documentation is available [here](https://exhbma.readthedocs.io).\nYou can try sample notebooks in the [tutorials](/tutorials) directory.\n\n# Reference paper\nIf you use this package in your research, please cite the following paper where the package was originally introduced: ["Data integration for multiple alkali metals in predicting coordination energies based on Bayesian inference"](https://doi.org/10.1080/27660400.2022.2108353).\n\nBibTeX entry:\n```\n@article{obinata2022data,\n  title={Data integration for multiple alkali metals in predicting coordination energies based on Bayesian inference},\n  author={Obinata, Koki and Nakayama, Tomofumi and Ishikawa, Atsushi and Sodeyama, Keitaro and Nagata, Kenji and Igarashi, Yasuhiko and Okada, Masato},\n  journal={Science and Technology of Advanced Materials: Methods},\n  volume={2},\n  number={1},\n  pages={355--364},\n  year={2022},\n  publisher={Taylor \\& Francis}\n}\n```\n',
    'author': 'Koki Obinata',
    'author_email': 'koki.obi.321@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/okada-lab/exhbma',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
