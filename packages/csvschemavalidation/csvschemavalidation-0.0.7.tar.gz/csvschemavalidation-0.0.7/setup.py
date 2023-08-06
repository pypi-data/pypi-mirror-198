#!/usr/bin/python
# -*-coding: utf-8 -*-

from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open("README.md") as f:
    long_description = f.read()

setup(
    name="csvschemavalidation",
    version="0.0.7",
    description="csvschemavalidation is an implementation of CSV Schema in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yassine Nifa",
    author_email="yasine.nifa@gmail.com",
    license="MIT",
    packages=["csvschemavalidation", "csvschemavalidation.validators"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="csv schema json jsonschema validation validator",
    url="https://github.com/YasineNifa/PyCSVSchema",
    install_requires=["jsonschema", "rfc3986", "pycountry"],
    package_data={"csvschemavalidation": ["schema.json"]},
    include_package_data=True,
)
