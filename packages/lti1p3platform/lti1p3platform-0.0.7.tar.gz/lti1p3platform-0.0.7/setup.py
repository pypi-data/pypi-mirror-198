# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lti1p3platform',
 'lti1p3platform.framework',
 'lti1p3platform.framework.django',
 'lti1p3platform.framework.fastapi']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT==1.7.1', 'jwcrypto>=1.4.2,<2.0.0', 'requests[security]==2.24.0']

setup_kwargs = {
    'name': 'lti1p3platform',
    'version': '0.0.7',
    'description': 'LTI 1.3 Platform implementation',
    'long_description': None,
    'author': 'Jun Tu',
    'author_email': 'jun@openlearning.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
