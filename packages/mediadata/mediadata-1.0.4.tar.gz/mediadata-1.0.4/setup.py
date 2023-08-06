from setuptools import setup, find_packages

with open("mediadata/requirements.txt", "r") as f:
    required = f.read().splitlines()

setup(
    name="mediadata",
    version="1.0.4",
    author="Praveen",
    author_email="mspraveenkumar77@gmail.com",
    description="A wrapper tool for mediainfo tool",
    packages=find_packages(),
    install_requires=required,
    url="https://git.selfmade.ninja/mspraveenkumar77/mediadata_pkg",
    entry_points={
        "console_scripts": ["mediadata = mediadata.mediadata:main"],
    },
)
