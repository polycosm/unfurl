#!/usr/bin/env python
from setuptools import find_packages, setup


project = "unfurl"
version = "0.1.0"


url = "https://github.com/polycosm/unfurl"
long_description = f"See {url}"
try:
    with open("README.md") as file_:
        long_description = file_.read()
except IOError:
    pass


setup(
    name=project,
    version=version,
    license="Apache 2.0",
    description="URL-based file extraction and loading.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jesse Myers",
    url=url,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        "boto3>=1.9.253",
        "click>=7.0",
    ],
    entry_points={
        "console_scripts": [
            "unfurlcopy = unfurl.main:main",
        ],
        "unfurl.providers": [
            "file = unfurl.providers.file:FileProvider",
            "s3 = unfurl.providers.s3:S3Provider",
        ],
    },
    extras_require=dict(
        dist=[
            "bumpversion>=0.5.3",
            "pip>=19.3.1",
            "setuptools>=41.4.0",
            "twine>=2.0.0",
            "wheel>=0.33.6",
        ],
        lint=[
            "flake8>=3.7.8",
            "flake8-isort>=2.7.0",
            "flake8-print>=3.1.1",
        ],
        test=[
            "coverage>=4.5.4",
            "nose>=1.3.7",
            "PyHamcrest>=1.9.0",
        ],
        typehinting=[
            "mypy>=0.740.0",
        ],
    ),
)
