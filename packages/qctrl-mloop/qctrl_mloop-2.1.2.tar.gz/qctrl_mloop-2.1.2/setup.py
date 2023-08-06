# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qctrlmloop']

package_data = \
{'': ['*']}

install_requires = \
['M-LOOP>=3.3.2,<3.4.0', 'qctrl>=21.0.1,<22.0.0', 'toml>=0.10.0,<0.11.0']

extras_require = \
{':python_full_version >= "3.7.2" and python_version < "3.8"': ['numpy>=1.21.6,<2.0.0',
                                                                'scipy>=1.7.3',
                                                                'matplotlib>=3.2,<3.5.2'],
 ':python_version >= "3.8" and python_version < "3.11"': ['numpy>=1.23.5,<2.0.0',
                                                          'scipy>=1.9.3',
                                                          'matplotlib>=3.6.3']}

setup_kwargs = {
    'name': 'qctrl-mloop',
    'version': '2.1.2',
    'description': 'Q-CTRL M-LOOP',
    'long_description': '# Q-CTRL M-LOOP\n\nThe Q-CTRL M-LOOP Python package allows you to integrate Boulder Opal\nautomated closed-loop optimizers with automated closed-loop optimizations\nmanaged by the open-source package M-LOOP.\n',
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': '',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.2,<3.11',
}


setup(**setup_kwargs)
