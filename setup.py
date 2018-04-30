from distutils.core import setup

with open('README.markdown') as file:
    long_description = file.read()

setup(
    name = 'dharmSentiment',
    packages = ['dharmSentiment'],
    package_data={'dharmSentiment': [
    'data/labMT/*.txt','data/PANAS-X/*.txt',
    'data/warriner/*.csv','data/ANEW/all*.csv', 'README.markdown', 'LICENSE.markdown',
    'data/MPQA-lexicon/subjectivity_clues_hltemnlp05/*.tff',
    'data/liu-lexicon/*-clean.txt','static/*.js','static/hedotools.shift.css']},
    version = '3.0.3',
    description = 'Basic usage script for dictionary-based sentiment analysis.\
    Intended use with labMT data. Modified for Dharmesh\'s personal use in CS 591 L1.',
    long_description = long_description,
    author = 'Dharmesh Tarapore',
    author_email = 'dharmesh@cs.bu.edu',
    url = 'https://github.com/weirdindiankid/dharmSentiment', 
    keywords = [],
    classifiers = ['Development Status :: 4 - Beta',
                   'Programming Language :: Python'],
    )





