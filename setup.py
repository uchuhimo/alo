# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='Alloy',
    version='0.2.0',
    description='A tool to combine function with DAG',
    python_requires='>=3.6',
    project_urls={
        "homepage": "https://github.com/uchuhimo/alloy",
        "repository": "https://github.com/uchuhimo/alloy"
    },
    author='uchuhimo',
    author_email='uchuhimo@outlook.com',
    license='Apache-2.0',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    entry_points={"console_scripts": ["alloy = alloy.cli:main"]},
    packages=['alloy'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'click', 'contextvars; python_version < "3.7"',
        'dataclasses; python_version < "3.7"', 'more-itertools', 'six',
        'typing; python_version < "3.7"', 'typing-extensions'
    ],
    extras_require={
        "dev": [
            "black", "bump2version", "coverage", "dephell[full]", "fissix",
            "flake8", "ipython", "isort", "mypy", "pip", "pre-commit", "pytest",
            "sphinx", "tox", "twine", "watchdog", "wheel"
        ]
    },
)
