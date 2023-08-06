# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['led_cube_data', 'led_cube_data.parser']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'construct>=2.10.68,<3.0.0', 'kaitaistruct>=0.10,<0.11']

setup_kwargs = {
    'name': 'led-cube-data',
    'version': '1.1.0',
    'description': 'File specification used in my LED cube projects.',
    'long_description': '# led-cube-data\nFile specification used in my LED cube projects. This is still in alpha and expected to change a lot as I work out the praticality of implementing the specification with my projects.\nCurrently, this package only includes parsers, serializers, and assemblers for Python.\n\nThe file specification is defined in ksy files and an ods spreadsheet. Both can be found [here](doc/file_specification).\nUnder the objects folder are more ksy files and test binaries.\n\nParsers for other languages can be made easily via the [Kaitai Struct compiler](https://kaitai.io/).\nOnly [parser.ksy](doc/file_specification/parser.ksy) needs to be compiled.\nIt references the other ksy files located under the objects folder and will be compiled as well.\n',
    'author': 'crash8229',
    'author_email': 'mu304007@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/crash8229/led-cube-data',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
