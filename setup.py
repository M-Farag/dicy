#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

# with open('HISTORY.rst') as history_file:
#     history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Mina Amin",
    author_email='mina.farag@icloud.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Simple Dice rolling package",
    entry_points={
        'console_scripts': [
            'dicy=dicy.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n',
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='dicy',
    name='dicy',
    packages=find_packages(include=['dicy', 'dicy.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/M-Farag/dicy',
    version='0.0.3',
    zip_safe=False,
)
