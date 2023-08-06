from setuptools import setup, find_packages

VERSION = '1.0'
DESCRIPTION = 'banga-python'
LONG_DESCRIPTION = 'A comprehensive package for bangla language processing in python.'

# Setting up
setup(
    name="bangla-python",
    version=VERSION,
    author="Nahid Hossain (nahidhossain)",
    author_email="mailbox.nahid@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['bangla-python', 'bangla language processing', 'bangla tokenizer', 'bangla remove punctuation', 'bangla number to word'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)