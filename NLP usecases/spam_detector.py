# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:53:27 2018

@author: Satya
"""

import pandas as pd
import numpy as np


data = pd.read_csv('./data/spambase/spambase.data').as_matrix()
np.random.shuffle(data)

trainX = data[:-100,:57]
trainY = data[:-100,-1]

testX = data[-100:,:57]
testY = data[-100:,-1]

from sklearn.naive_bayes import MultinomialNB as M
model = M()
model.fit(trainX,trainY)
print('Model training accuracy: ',model.score(trainX,trainY))
print('Model testing accuracy: ',model.score(testX,testY))


from sklearn.ensemble import AdaBoostClassifier as M
model = M()
model.fit(trainX,trainY)
print('Model training accuracy: ',model.score(trainX,trainY))
print('Model testing accuracy: ',model.score(testX,testY))

