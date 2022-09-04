from setuptools import setup
from pathlib import Path

import stopwatch

description = "A simple stopwatch for python"
long_description = Path("README.rst").read_text("utf-8")

setup(
    name="stopwatch.py",
    version=stopwatch.__version__,
    description=description,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ravener/stopwatch.py",
    author=stopwatch.__author__,
    author_email="ravener.anime@gmail.com",
    license=stopwatch.__license__,
    py_modules=["stopwatch"],
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
