from setuptools import setup

setup(
    name="contu",
    version="0.1",
    author="Harshul Nanda",
    author_email="harshulnanda0@gmail.com",
    description="A simple package that converts contracted forms of words to their uncontracted counterparts with lowercasing the each word.",
    packages=["contu"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)