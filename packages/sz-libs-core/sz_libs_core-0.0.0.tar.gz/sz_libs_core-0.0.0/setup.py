# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sz_core',
 'sz_core.configs',
 'sz_core.encoders',
 'sz_core.enums',
 'sz_core.exceptions',
 'sz_core.ext.consul',
 'sz_core.ext.fastapi',
 'sz_core.ext.fastapi.handlers',
 'sz_core.ext.fastapi.schemas',
 'sz_core.ext.fastapi.test_utils',
 'sz_core.ext.graphql',
 'sz_core.ext.graphql.extensions',
 'sz_core.ext.graphql.utils',
 'sz_core.pydantic']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0,<1', 'pydantic[dotenv]>=1,<2']

extras_require = \
{'consul': ['python-consul2>=0,<1'],
 'fastapi': ['fastapi>=0,<1'],
 'graphql': ['gql[aiohttp]>=3,<4', 'ariadne>=0,<1', 'aiofiles>=23,<24']}

setup_kwargs = {
    'name': 'sz-libs-core',
    'version': '0.0.0',
    'description': 'Core selfzen library',
    'long_description': '# Selfzen - Core backend library\n\nCore library for Selfzen services\n',
    'author': 'Ivan Galin',
    'author_email': 'i.galin@devartsteam.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/selfzen/backend/libs/core',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.11,<3.12',
}


setup(**setup_kwargs)
