from setuptools import setup, find_packages

with open("mediadata/requirements.txt", "r") as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mediadata",
    version="1.0.7",
    author="Praveen",
    author_email="mspraveenkumar77@gmail.com",
    description="A wrapper tool for mediainfo tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=required,
    url="https://git.selfmade.ninja/mspraveenkumar77/mediadata_pkg",
    entry_points={
        "console_scripts": ["mediadata = mediadata.mediadata:main"],
    },
)
