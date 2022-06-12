from setuptools import setup, find_packages

description = "A simple stopwatch for python"

long_description = ""

with open("README.rst") as f:
    long_description = f.read()

version = "1.1.0"

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
    packages=find_packages(exclude=["test"]),
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
