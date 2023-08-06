#!/usr/bin/env python3

import os
import setuptools
from setuptools import find_packages, setup

pkg_dir = os.path.abspath(__file__ + '/..')

setup(
    name='reasoningchain',
    version='0.0.11',
    author='duer',
    long_description=open(os.path.join(pkg_dir, "README.md")).read(),
    long_description_content_type='text/markdown',
    python_requires = '>=3.7.0',
    packages = find_packages(),
    install_requires=[
        "langchain",
        "click",
        "openai",
        "LAC",
        "tqdm",
        "streamlit",
    ],
)

