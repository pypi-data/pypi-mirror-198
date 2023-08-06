import pathlib
import re
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# The text of the CHANGELOG file
CHANGELOG = (HERE / "CHANGELOG.md").read_text()


def find_version(filename):
    _version_re = re.compile(r'__version__ = "(.*)"')
    for line in open(filename):
        version_match = _version_re.match(line)
        if version_match:
            return version_match.group(1)

VERSION = find_version("ldpy/__init__.py")

PACKAGES = find_packages(exclude=("examples*", "test*"))

# This call to setup() does all the work
setup(
    name="linked-data-python",
    version=VERSION,
    description="The python package \"linked-data-python\" can execute .ldpy files and run an interactive ldpy console.",
    author="Maxime Lefrançois",
    author_email="maxime.lefrancois@emse.fr",
    url="https://gitlab.com/coswot/ldpy",
    license="MIT",
    platforms=["any"],
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    long_description=README + "\n" + CHANGELOG,
    long_description_content_type="text/markdown",
    packages=PACKAGES,
    include_package_data=True,
    install_requires=["antlr4-python3-runtime", "rdflib", "ideas"],
    entry_points={
        "console_scripts": [
            "ldpy=ldpy.__main__:main",
        ]
    },
)
