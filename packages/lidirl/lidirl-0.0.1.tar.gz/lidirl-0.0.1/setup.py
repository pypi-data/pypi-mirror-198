

#!/usr/bin/env python

"""
A setuptools based setup module.
See:
- https://packaging.python.org/en/latest/distributing.html
- https://github.com/pypa/sampleproject
To install:
1. Setup pypi by creating ~/.pypirc
        [distutils]
        index-servers =
          pypi
          pypitest
        [pypi]
        username=
        password=
        [pypitest]
        username=
        password=
2. Create the dist
   python3 setup.py sdist bdist_wheel
3. Push
   twine upload dist/*
"""

import os
import re

# Always prefer setuptools over distutils
from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)


def get_version():
    """
    Reads the version from ersatz's __init__.py file.
    We can't import the module because required modules may not
    yet be installed.
    """
    VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')
    init = open(os.path.join(ROOT, 'lidirl', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


def get_description():
    DESCRIPTION_RE = re.compile(r'''__description__ = ['"](.*)['"]''')
    init = open(os.path.join(ROOT, 'lidirl', '__init__.py')).read()
    return DESCRIPTION_RE.search(init).group(1)



setup(
    name = 'lidirl',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version = get_version(),

    description = get_description(),

    long_description = "LIDIRL is a simple toolkit for LID targeting noisy spontaneous text as one might find in internet data."
                        "It allows for training custom models or using a pretrained solution.",

    url = "https://github.com/rewicks/lidirl/",

    author = "Rachel Wicks",
    author_email = "rewicks@jhu.edu",
    maintainer_email = "rewicks@jhu.edu",

    license = "Apache License 2.0",

    python_requires = ">=3",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3 :: Only',
    ],

    # What does your project relate to?
    keywords = ["language identification", "lid", "langid", "data processing", "preprocessing", "NLP", "natural language processing", "comptuational linguistics"],

    # Which packages to deploy?
    packages = find_packages(),
    
    # Mark lidirl (and recursively all its sub-packages) as supporting mypy type hints (see PEP 561).
    package_data={"lidirl": ["py.typed"]},

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires = [
        'typing;python_version<"3.5"',
        'numpy>= 1.20',
        'torch>=1.11.0',
        'torchmetrics>=0.8.2',
        'torchvision>=0.8.2',
        'transformers>=4.22.0',
        'uncertainty-metrics>=0.0.81',
        'flopth>=0.0.502',
        'xxhash>=3.0.0',
        ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require = {},

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'lidirl = lidirl.label:main',
            'lidirl_train = lidirl.trainer:main',
            'lidirl_preprocess = lidirl.dataset:main'
        ],
    },

    )
