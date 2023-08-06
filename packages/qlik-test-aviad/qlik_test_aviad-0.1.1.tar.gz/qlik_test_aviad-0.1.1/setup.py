# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qlik_test_aviad']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4,<2.0']

setup_kwargs = {
    'name': 'qlik-test-aviad',
    'version': '0.1.1',
    'description': '',
    'long_description': '# qlik-test-aviad\n \nthis amazing project does something!',
    'author': 'Aviad Rozenhek',
    'author_email': 'aviadr1@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
