from setuptools import setup, find_packages

setup(
    name="my_red",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)