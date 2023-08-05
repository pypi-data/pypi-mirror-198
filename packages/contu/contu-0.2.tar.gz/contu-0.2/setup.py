from setuptools import setup

setup(
    name="contu",
    version="0.2",
    author="Harshul Nanda",
    author_email="harshulnanda0@gmail.com",
    description="A simple package that converts contracted forms of words to their uncontracted counterparts.",
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