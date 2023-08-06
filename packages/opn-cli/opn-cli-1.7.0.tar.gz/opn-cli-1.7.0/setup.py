import os
from setuptools import setup, find_packages

from opnsense_cli import __cli_name__, __version__

_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=__cli_name__,
    version=__version__,
    packages=find_packages(),
    description="OPNsense CLI written in python.",
    author='Andreas Stürz IT-Solutions',
    license='BSD-2-Clause License',
    project_urls={
        'Bug Tracker': 'https://github.com/andeman/opnsense_cli/issues',
        'CI: GitHub Actions Pipelines': 'https://github.com/andeman/opnsense_cli/actions',
        'Documentation': 'https://github.com/andeman/opnsense_cli',
        'Source Code': 'https://github.com/andeman/opnsense_cli',
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'click>=8.0.1',
        'requests',
        'PTable',
        'PyYAML',
        'jsonpath-ng',
        'beautifulsoup4',
        'lxml',
        'Jinja2'
    ],
    python_requires='>=3.7',
    entry_points='''
        [console_scripts]
        opn-cli=opnsense_cli.cli:cli
    ''',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
