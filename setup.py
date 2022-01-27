import setuptools

description = "A simple stopwatch for python"

long_description = ""

with open("README.rst", "utf-8") as f:
    long_description = f.read()

version="1.0.1"

packages = ["stopwatch"]

setuptools.setup(
    name="stopwatch.py",
    version=version,
    description=description,
    long_description=long_description,
    url="https://github.com/freetnt5852/stopwatch.py",
    author="Free TNT",
    author_email="darksoulgamer5852@gmail.com",
    license="MIT",
    packages=packages,
    include_package_data=True
)
