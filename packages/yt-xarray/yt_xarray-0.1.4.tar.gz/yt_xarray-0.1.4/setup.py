#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("requirements.txt") as reqs_file:
    requirements = reqs_file.read().strip().split("\n")

with open("README.md", "r") as readme_file:
    readme_md = readme_file.read()


test_requirements = [
    "pytest>=3",
]

setup(
    author="Chris Havlin",
    author_email="chris.havlin@gmail.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="interface between yt and xarray",
    install_requires=requirements,
    license="MIT license",
    long_description=readme_md,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="yt_xarray",
    name="yt_xarray",
    packages=find_packages(include=["yt_xarray", "yt_xarray.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/data-exp-lab/yt_xarray",
    version="0.1.4",
    zip_safe=False,
)
