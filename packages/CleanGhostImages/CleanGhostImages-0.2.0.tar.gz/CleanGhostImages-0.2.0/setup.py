"""Install packages as defined in this file into the Python environment."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="CleanGhostImages",
    author="Ixonae",
    author_email="contact@ixonae.com",
    description="A tool to find unused images in the Ghost blog content directory",
    version="0.2.0",
    packages=find_packages(where=".", exclude=["tests"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    url="https://github.com/ixonae/CleanGhostImages",
    install_requires=[
        "setuptools>=45.0",
    ],
    entry_points={
        "console_scripts": [
            "cleanghostimages=cleanghostimages.__main__:main",
        ]
    },
    license="GNU GENERAL PUBLIC LICENSE v2"
)
