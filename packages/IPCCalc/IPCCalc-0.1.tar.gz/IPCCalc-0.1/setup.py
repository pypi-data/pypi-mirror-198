from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.1'
DESCRIPTION = 'Python package for computing inflation adjustment, with historic Spanish IPC data and peseta to euro conversion.'
LONG_DESCRIPTION = 'A Python package to quickly compute inflation adjustment for a sum of money, taking into account historic IPC (Índice de Precios de Consumo) data, and optionally converting amounts from pesetas to euros.'

# Setting up
setup(
    name="IPCCalc",
    version=VERSION,
    author="scuellaralmagro",
    author_email="<scuellaralmagro@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'inflation', 'ipc', 'pesetas', 'euros', 'spain', 'depreciation', 'adjustment', 'adjust'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)