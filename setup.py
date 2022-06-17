from setuptools import setup
from pathlib import Path

description = "A simple stopwatch for python"

long_description = Path("README.rst").read_text("utf-8")
version = "2.0.0"
packages = ["stopwatch"]

setup(
    name="stopwatch.py",
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ravener/stopwatch.py",
    author="Ravener",
    author_email="ravener.anime@gmail.com",
    license="MIT",
    packages=packages,
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
