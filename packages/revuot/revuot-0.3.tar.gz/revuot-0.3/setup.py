from setuptools import setup, find_packages
import codecs
import os



VERSION = '0.3'
DESCRIPTION = 'a reverse shell for testing perpose'
LONG_DESCRIPTION = 'A package that allows to make a backdoor that can be implemented with other programs as torjen with fetures of downloading and uploading files to tagted device'

# Setting up
setup(
    name="revuot",
    version=VERSION,
    author="hisamdavid (dawood hithem)",
    author_email="<deviddevid287@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'hacking', 'backdoor', 'tojen', 'reverse shell','cyper security'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)