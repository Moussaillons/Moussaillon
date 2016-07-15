import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "moussaillon",
    description = ("A CMS for associations federations"),
    long_description=read('README.md'),
    version = "0.0.1",
    author = "Louis Desportes & Moussaillon contributors",
    author_email = "louis@akkes.fr",
    license = "GNU AGPLv3+",
    keywords = "CMS associations",
    url = "http://akkes.fr/realisations/moussaillon/",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Natural Language :: French",
        "Operating System :: OS Independent",
    ],
    packages=['moussaillon'],
    install_requires=['flask', 'nose'],
)
