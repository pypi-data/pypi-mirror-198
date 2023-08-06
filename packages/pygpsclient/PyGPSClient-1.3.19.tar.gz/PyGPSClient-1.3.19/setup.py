#!/usr/bin/env python
"""
Setup script for PyGPSClient Application

python setup.py sdist bdist_wheel

Created on 12 Sep 2020

:author: semuadmin
"""

from setuptools import setup, find_namespace_packages
from pygpsclient import version as VERSION

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PyGPSClient",
    version=VERSION,
    packages=find_namespace_packages(
        exclude=["tests", "references", "images", "docs", "examples"],
    ),
    install_requires=[
        "pygnssutils>=1.0.5",
        "requests>=2.28.0",
        "Pillow>=9.0.0",
        "pyserial>=3.5",
        "pyspartn>=0.1.3",
    ],
    package_data={
        "pygpsclient": [
            "resources/*.gif",
            "resources/*.png",
            "resources/*.ico",
            "resources/*.icns",
        ],
    },
    entry_points={
        "console_scripts": [
            "pygpsclient = pygpsclient.__main__:main",
        ]
    },
    include_package_data=True,
    author="semuadmin",
    author_email="semuadmin@semuconsulting.com",
    description="PyGPSClient GNSS/GPS Graphical Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/semuconsulting/PyGPSClient",
    license="BSD 3-Clause 'Modified' License",
    keywords="PyGPSClient GNSS GPS GLONASS BEIDOU NMEA UBX RTCM NTRIP SPARTN RTK DGPS",
    platforms="Windows, MacOS, Linux",
    project_urls={
        "Home Page": "https://www.semuconsulting.com/pygpsclientgui",
        "Documentation": "https://www.semuconsulting.com/pygpsclient",
        "Source Code": "https://github.com/semuconsulting/PyGPSClient",
        "Bug Tracker": "https://github.com/semuconsulting/PyGPSClient",
    },
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: MacOS X",
        "Environment :: X11 Applications",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Desktop Environment",
        "Topic :: Terminals :: Serial",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    python_requires=">=3.7",
)
