# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['solid2_extensions',
 'solid2_extensions.BOSL',
 'solid2_extensions.BOSL.examples',
 'solid2_extensions.BOSL.tests',
 'solid2_extensions.BOSL2',
 'solid2_extensions.MCAD',
 'solid2_extensions.MCAD.bitmap',
 'solid2_extensions.PolyGear',
 'solid2_extensions.examples',
 'solid2_extensions.scad.BOSL.scripts',
 'solid2_extensions.scad.BOSL2.scripts',
 'solid2_extensions.scad.MCAD']

package_data = \
{'': ['*'],
 'solid2_extensions': ['scad/BOSL/*',
                       'scad/BOSL/examples/*',
                       'scad/BOSL/tests/*',
                       'scad/BOSL2/*',
                       'scad/BOSL2/images/*',
                       'scad/BOSL2/tests/*',
                       'scad/BOSL2/tutorials/*',
                       'scad/PolyGear/*',
                       'scad/PolyGear/examples/*'],
 'solid2_extensions.scad.MCAD': ['bitmap/*']}

install_requires = \
['solidpython2>=2.0.0-beta.3,<3.0.0']

setup_kwargs = {
    'name': 'solidpython2-extensions',
    'version': '0.1.4',
    'description': 'some extensions for solidpython2',
    'long_description': 'None',
    'author': 'jeff',
    'author_email': '1105041+jeff-dh@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
