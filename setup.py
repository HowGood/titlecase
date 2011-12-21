import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()

sys.path.insert(0, here)

from titlecase import __version__

setup(name='titlecase',
    version=__version__,
    description="Python Port of John Gruber's titlecase.pl",
    long_description=README,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Text Processing :: Filters",
    ],
    keywords='string formatting',
    author="Stuart Colville",
    author_email="pypi@muffinresearch.co.uk",
    url="http://muffinresearch.co.uk/",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    tests_require=['nose'],
    test_suite="titlecase.tests",
    entry_points = """\
    """
)

