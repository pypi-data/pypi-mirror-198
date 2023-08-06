"""Package setup"""
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    "lxml",
    "beautifulsoup4",
    "requests",
    "fake_useragent"
]

setup(
    name="youtube-webscrape-api",
    version="0.0.1",
    author="Muhammad Huzaifa",
    author_email="muhammadhuzaifagamer123@gmail.com",
    url="https://github.com/huzai786/Youtube-Scraper",
    description="Webscrape based youtube api, free of cost",
    license="MIT",
    packages=find_packages(exclude=['test']),
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['youtube-api', 'youtube-scraper', 'Youtube-scrape'],
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
