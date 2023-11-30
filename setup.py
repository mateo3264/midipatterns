from setuptools import setup, find_packages
import codecs
import os



VERSION = '0.0.3'
DESCRIPTION = 'Detect midi patterns'
LONG_DESCRIPTION = 'A package that allows to detect midi patterns.'

# Setting up
setup(
    name="midipatternspkg",
    version=VERSION,
    author="Mateo Acosta",
    author_email="<maacostaro@unal.edu.co>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pygame', 'music21'],
    keywords=['python', 'midi', 'piano'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)