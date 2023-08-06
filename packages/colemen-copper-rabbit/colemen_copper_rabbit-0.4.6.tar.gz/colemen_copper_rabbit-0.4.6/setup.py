import os
# from glob import glob
from setuptools import setup, find_packages
import colemen_utilities.build_utils.general as _gen


VERSION='0.4.6'
DESCRIPTION = 'copper_rabbit'
LONG_DESCRIPTION = 'Practicing the sql alchemy ORM with the equari database as a separate library'


_root_path = f"{os.getcwd()}/copper_rabbit"
PY_MODULES = _gen.list_py_modules(
    _root_path,
    additions=['main']
)
_gen.purge_dist()

DATA_FILES = [
    # ('Lib/site-packages/copper_rabbit/documentation', glob('documentation/*.md')),
    # ('where the files will be installed', glob('where to get the files to include')),
]

# Setting up
setup(
    name="colemen_copper_rabbit",
    version=VERSION,
    author="Colemen Atwood",
    author_email="<atwoodcolemen@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    py_modules=PY_MODULES,
    # add any additional packages that
    # need to be installed along with your package. Eg: 'caer'
    install_requires=[
        'colemen_utils',
        'flask',
        'pyjwt',
        'passlib',
        'sqlalchemy_utils',
        'flask_smorest',
    ],

    keywords=['python'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
