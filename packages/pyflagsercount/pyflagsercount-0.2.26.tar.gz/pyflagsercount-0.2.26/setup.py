# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyflagsercount',
 'pyflagsercount.pybind11',
 'pyflagsercount.pybind11.docs',
 'pyflagsercount.pybind11.pybind11',
 'pyflagsercount.pybind11.tests',
 'pyflagsercount.pybind11.tests.extra_python_package',
 'pyflagsercount.pybind11.tests.extra_setuptools',
 'pyflagsercount.pybind11.tests.test_cmake_build',
 'pyflagsercount.pybind11.tests.test_embed',
 'pyflagsercount.pybind11.tools']

package_data = \
{'': ['*'],
 'pyflagsercount': ['include/*', 'src/*'],
 'pyflagsercount.pybind11': ['.git/*',
                             '.git/hooks/*',
                             '.git/info/*',
                             '.git/logs/*',
                             '.git/logs/refs/heads/*',
                             '.git/logs/refs/remotes/origin/*',
                             '.git/objects/pack/*',
                             '.git/refs/heads/*',
                             '.git/refs/remotes/origin/*',
                             '.github/*',
                             '.github/ISSUE_TEMPLATE/*',
                             '.github/matchers/*',
                             '.github/workflows/*',
                             'include/pybind11/*',
                             'include/pybind11/detail/*',
                             'include/pybind11/eigen/*',
                             'include/pybind11/stl/*'],
 'pyflagsercount.pybind11.docs': ['_static/css/*',
                                  'advanced/*',
                                  'advanced/cast/*',
                                  'advanced/pycpp/*',
                                  'cmake/*'],
 'pyflagsercount.pybind11.tests.test_cmake_build': ['installed_embed/*',
                                                    'installed_function/*',
                                                    'installed_target/*',
                                                    'subdirectory_embed/*',
                                                    'subdirectory_function/*',
                                                    'subdirectory_target/*']}

install_requires = \
['numpy>=1.17.0', 'pybind11>=2.8.0,<3.0.0']

setup_kwargs = {
    'name': 'pyflagsercount',
    'version': '0.2.26',
    'description': 'A program for counting directed cliques in directed graphs',
    'long_description': '# flagser-count\nA program for counting directed cliques in directed graphs, adapted from https://github.com/luetge/flagser\n\nA python version called pyflagsercount is available from pypi and can be installed with\n```sh\npip install pyflagsercount\n```\n\nTo install from this repo, first download repository with:\n```sh\ngit clone --recursive https://github.com/JasonPSmith/flagser-count.git\n```\nNext, compile flagser count with\n```\nmake\n```\n\nTo verify that flagser-count has installed correctly run:\n\n```sh\n(cd test && python run_test.py && cd ..)\n```\n\nTo install pyflagsercount run:\n```sh\npip install .\n```\nRequirements: For pyflagsercount the packages numpy and pybind11 are required, and cmake version ≥ 2.8.12.\n',
    'author': 'jasonpsmith',
    'author_email': 'jasonsmith.bath@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
