#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-bamboohr",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_bamboohr"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        # Added wheel
        "wheel==0.37.0",
        "singer-python==5.12.2",
        "requests==2.26.0",
        "PyBambooHR==0.8.1"
    ],
    entry_points="""
    [console_scripts]
    tap-bamboohr=tap_bamboohr:main
    """,
    packages=["tap_bamboohr"],
    package_data = {
        "schemas": ["tap_bamboohr/schemas/*.json"]
    },
    include_package_data=True,
)
