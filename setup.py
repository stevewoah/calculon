"""Setup script for the calculon package."""

from setuptools import setup, find_packages

setup(
    name="calculon",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "calculon=calculon.main:main"  # Points to the main function in main.py
        ]
    },
    author="Your Name",
    description="A simple calculator in Python",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
