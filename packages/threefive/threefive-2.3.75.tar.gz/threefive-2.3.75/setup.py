#!/usr/bin/env python3


import setuptools
import threefive
#from Cython.Build import cythonize

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name="threefive",
    version=threefive.version(),
    author="Adrian",
    author_email="spam@iodisco.com",
    description="Pythonic SCTE35",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/futzu/threefive",
    install_requires=[
        "new_reader >= 0.1.3",
        "pyaes",
    ],
    scripts=["bin/threefive"],
#    ext_modules=cythonize("threefive/*.py", language_level="3"),
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=3.6",
)
