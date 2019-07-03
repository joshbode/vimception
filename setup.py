#! /usr/bin/env python

from setuptools import setup

setup(
    name="vimception",
    description="Vim Exceptions",
    long_description=open("README.md", "rt").read().strip(),
    long_description_content_type="text/markdown",
    author="Josh Bode",
    author_email="joshbode@fastmail.com",
    url="https://github.com/joshbode/vimception/",
    license="MIT",
    package="vimception",
    packages=["vimception"],
    install_requires=["autowrapt"],
    entry_points={
        'vimception': ['sys = vimception:replace_excepthook'],
    }
)
