from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path
import re

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/__init__.py').read())
    return result.group(1)

# This call to setup() does all the work
setup(
    name="gtdownloader",
    version=get_property('__version__', 'gtdownloader'),
    description="A Python package for the simple downloading of tweets with geographical information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gtdownloader.readthedocs.io/",
    author="Juan G Acosta",
    author_email="jgacostas@icloud.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["gtdownloader", "gtdownloader/_utils"],
    include_package_data=True,
    install_requires=["requests",
                      "pandas>=1.3.2",
                      "geopandas>=0.10.2",
                      "matplotlib>=3.4.3",
                      "seaborn>=0.11.2",
                      "shapely>=1.8.0",
                      "wordcloud>=1.8.2.2",
                      "plotly>=5.5.0",
                      "pyyaml"]
)