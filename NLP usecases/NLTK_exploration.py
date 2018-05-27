# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:03:54 2018

@author: Satya
"""

# POS tagger
import nltk
print(nltk.pos_tag("Machine learning is a great course".split()))


# Stemming
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('wolves'))

# Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('wolves'))

s = "Barack Obama was born in Huwai"
tags = nltk.pos_tag(s.split())
print(tags)
ner = nltk.ne_chunk(tags)
print(ner)
nltk.ne_chunk(tags).draw()