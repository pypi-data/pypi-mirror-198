# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mabby', 'mabby.simulation', 'mabby.strategies']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.7.0,<4.0.0', 'numpy>=1.24.2,<2.0.0']

setup_kwargs = {
    'name': 'mabby',
    'version': '0.1.1',
    'description': 'A multi-armed bandit (MAB) simulation library',
    'long_description': '<h1 align="center">\n<img src="https://raw.githubusercontent.com/ew2664/mabby/main/assets/mabby-logo-title.png" width="500">\n</h1>\n\n[![license](https://img.shields.io/github/license/ew2664/mabby)](https://github.com/ew2664/mabby/blob/main/LICENSE)\n[![issues](https://img.shields.io/github/issues/ew2664/mabby)](https://github.com/ew2664/mabby/issues)\n[![build](https://img.shields.io/github/actions/workflow/status/ew2664/mabby/ci.yml)](https://github.com/ew2664/mabby/actions/workflows/ci.yml)\n[![coverage](https://coveralls.io/repos/github/ew2664/mabby/badge.svg)](https://coveralls.io/github/ew2664/mabby)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)\n[![poetry](https://img.shields.io/badge/packaging-poetry-008adf)](https://python-poetry.org/)\n[![black](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)\n[![mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)\n\n**mabby** is a library for simulating [multi-armed bandits (MABs)](https://en.wikipedia.org/wiki/Multi-armed_bandit), a resource-allocation problem and framework in reinforcement learning. It allows users to quickly yet flexibly define and run bandit simulations, with the ability to:\n\n- choose from a wide range of classic bandit algorithms to use\n- configure environments with custom arm spaces and rewards distributions\n- collect and visualize simulation metrics like regret and optimality\n\n## Installation\n\nInstall **mabby** with `pip`:\n\n```bash\npip install mabby\n```\n\n## Examples\n\n- [**Bernoulli Bandits**](./examples/bernoulli_bandit.py): a four-armed Bernoulli bandit simulation comparing epsilon-greedy, UCB1, and Thompson sampling strategies\n\n## Contributing\n\nPlease see [CONTRIBUTING](CONTRIBUTING.md) for more information.\n\n## License\n\nThis software is licensed under the Apache 2.0 license. Please see [LICENSE](LICENSE) for more information.\n',
    'author': 'Ethan Wu',
    'author_email': 'ew2664@columbia.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
