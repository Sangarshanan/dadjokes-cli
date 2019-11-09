# -*- coding: utf-8 -*-
from setuptools import find_packages
from dadjokes import (
	__version__,
	__title__,
    __url__,
    __description__,
    __author__,
    __author_email__
)
with open("README.md", "r") as f:
    readme = f.read()

requires = [
    "Click==7.0",
    "beautifulsoup4==4.8.1",
    "cowpy==1.1.0",
    "requests==2.22.0",
    "cachetools==3.1.1"
]
dev_requires = ["pytest==5.2.2"]
dev_requires = dev_requires + requires


def setup_package():
    metadata = dict(
        name=__title__,
        version= __version__,
        description=__description__,
        long_description=readme,
        long_description_content_type="text/markdown",
        author=__author__,
        author_email = __author_email__,
        url = __url__,
        packages=find_packages(exclude=("tests",)),
        install_requires=requires,
        extras_require={"dev": dev_requires},
        entry_points={"console_scripts": ["dadjoke = dadjokes.cli:cli"]},
    )

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
