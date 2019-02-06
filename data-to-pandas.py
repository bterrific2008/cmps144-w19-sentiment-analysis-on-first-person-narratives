import os
from hidden import filePath
import numpy as np
import pandas as pd

idPhrase = []
sentiment = []

# obtain all instances of development data with negative sentiment
fileNames = os.listdir(filePath + "train/neg/")
negSentences = []
for i in range(1, len(fileNames)):
    file = open(filePath + "train/neg/" + fileNames[i], 'r')
    negSentences.append(file.read())
    idPhrase.append(fileNames[i])
    sentiment.append("0")
print(len(negSentences))

# turn the assembled array of negative sentences into a pandas serries
negSeries = pd.Series(negSentences)

# obtain all instances of dev data with positive sentiment
fileNames = os.listdir(filePath + "train/pos/")
posSentences = []
for i in range(1, len(fileNames)):
    file = open(filePath + "train/pos/" + fileNames[i], 'r')
    posSentences.append(file.read())
    idPhrase.append(fileNames[i])
    sentiment.append("1")
print(len(posSentences))

# assembles everything into a Pandas dataframe
d = {'id': pd.Series(idPhrase), 'sentence': pd.Series(negSentences+posSentences), 'sentiment': pd.Series(sentiment)}
df = pd.DataFrame(d)
print(df.index)
print(df.columns)
df.to_csv("sentences.csv")