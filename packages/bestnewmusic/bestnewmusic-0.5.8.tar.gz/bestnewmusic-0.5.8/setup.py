from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read().split("\n")

setup(
    name="bestnewmusic",
    description="View music reviews and weekly radio charts in the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ddbourgin/bestnewmusic",
    version="0.5.8",
    author="David Bourgin",
    author_email="ddbourgin@gmail.com",
    license="MIT",
    keywords=["music", "terminal"],
    packages=["bestnewmusic"],
    entry_points={"console_scripts": ["bnm = bestnewmusic.__main__:main"]},
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
    ],
    project_urls={"Source": "https://github.com/ddbourgin/bestnewmusic"},
)
