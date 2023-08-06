"""Package setup"""
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    "webdriver_manager",
    "beautifulsoup4",
    'selenium',
    "lxml",
]

setup(
    name="Google-Paa-Scraper",
    version="0.0.11",
    author="Muhammad Huzaifa",
    author_email="muhammadhuzaifagamer123@gmail.com",
    url="https://github.com/huzai786/Google-Paa-Scraper",
    description="Get data from googles people also ask section.",
    license="MIT",
    packages=find_packages(exclude=['tests']),
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['google-paa', 'People-Also-Ask', 'Google-PAA'],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers"
    ],
)
