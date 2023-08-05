from setuptools import setup

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="contu",
    version="0.3",
    author="Harshul Nanda",
    author_email="harshulnanda0@gmail.com",
    description="A simple package that converts contracted forms of words to their uncontracted counterparts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["contu"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Harshul-18/contu.git",
    python_requires='>=3.0',
    install_requires=[
        "nltk",
    ]
)