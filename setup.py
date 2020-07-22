"""Setup script for pybites-tips"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybites-tips",
    version="0.0.1",
    author="PyBites",
    author_email="support@pybit.es",
    description="Search for PyBites tips via the command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pybites/tips",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
