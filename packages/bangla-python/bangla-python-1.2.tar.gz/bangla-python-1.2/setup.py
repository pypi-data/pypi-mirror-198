from setuptools import setup, find_packages

VERSION = '1.2'
DESCRIPTION = 'bangla-python'
LONG_DESCRIPTION = 'A comprehensive package for bangla language processing in python.<br> Please full documentation: http://www.nahid.org/bangla-python '

# Setting up
setup(
    name="bangla-python",
    version=VERSION,
    author="Nahid Hossain (nahid@cse.uiu.ac.bd)",
    author_email="mailbox.nahid@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['bangla-python', 'bangla language processing', 'bangla tokenizer', 'bangla remove punctuation','bangla remove foreign word', 'bangla number to word','bangla numbers', 'bangla to english number','english to bangla number','bangla number to word'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)