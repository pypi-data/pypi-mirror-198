# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yapona']

package_data = \
{'': ['*']}

install_requires = \
['dbus-next>=0.2.3,<0.3.0', 'pygobject>=3.42.2,<4.0.0']

setup_kwargs = {
    'name': 'yapona',
    'version': '0.1.0',
    'description': 'Pomodoro timer',
    'long_description': '# Yapona\n\nYet another Pomodoro Timer...\n',
    'author': 'Dima Lipin',
    'author_email': 'dimich3d@ya.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
