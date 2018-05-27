# -*- coding: utf-8 -*-
"""
Created on Sat May 26 18:53:34 2018

@author: Satya
"""

import nltk
from nltk.stem import WordNetLemmatizer
from stop_words import get_stop_words


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

lemmatizer = WordNetLemmatizer()
stopwords = get_stop_words('english')
# \data\domain_sentiment_data\sorted_data_acl\books

pos_reviews = BeautifulSoup(open('./data/domain_sentiment_data/sorted_data_acl/books/positive.review').read(),"lxml")
pos_reviews = pos_reviews.findAll('review_text')


neg_reviews = BeautifulSoup(open('./data/domain_sentiment_data/sorted_data_acl/books/negative.review').read(),"lxml")
neg_reviews = neg_reviews.findAll('review_text')

print(len(pos_reviews))
print(len(neg_reviews))

np.random.shuffle(pos_reviews)
pos_reviews = pos_reviews[:len(neg_reviews)]


word_index_map = {}
index = 0

pos_tokenized = []
neg_tokenized = []

def my_tokenizer(s):
    s= s.lower()
    tokens = nltk.tokenize.word_tokenize(s)
    tokens = [w for w in tokens if len(w) > 2]
    tokens = [lemmatizer.lemmatize(w) for w in tokens]
    tokens = [w for w in tokens if w not in stopwords]
    
    return tokens

def tokens_to_vector(tokens, label):
    x = np.zeros(len(word_index_map)+1)
    for t in tokens:
        i = word_index_map[t]
        x[i]+=1
    x = x/x.sum()
    x[-1] = label
    return x


for review in pos_reviews:
    tokens = my_tokenizer(review.text)
    pos_tokenized.append(tokens)
    for token in tokens:
        if token not in word_index_map:
            word_index_map[token] = index
            index += 1
            
for review in neg_reviews:
    tokens = my_tokenizer(review.text)
    neg_tokenized.append(tokens)
    for token in tokens:
        if token not in word_index_map:
            word_index_map[token] = index
            index += 1
            
N = len(pos_tokenized) + len(neg_tokenized)
data = np.zeros((N,len(word_index_map)+1))

i=0
for tokens in pos_tokenized:
    v = tokens_to_vector(tokens, 1)
    data[i,:] = v
    i+=1
for tokens in neg_tokenized:
    v = tokens_to_vector(tokens, 0)
    data[i,:] = v
    i+=1
           
np.random.shuffle(data)

trainX = data[:-100,:len(word_index_map)]
trainY = data[:-100,-1]

testX = data[-100:,:len(word_index_map)]
testY = data[-100:,-1]

from sklearn.linear_model import LogisticRegression as M
model = M()
model.fit(trainX,trainY)
print("Model train score is: ",model.score(trainX,trainY))
print("Model test score is: ",model.score(testX,testY))



th = 0.5
for word, index in word_index_map.items():
    weight = model.coef_[0][index]
    if weight >th or weight<-th:
        print(word,weight)