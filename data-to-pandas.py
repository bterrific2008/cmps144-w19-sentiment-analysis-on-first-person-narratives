import os
from hidden import filePath
import numpy as np
import pandas as pd

# obtain all instances of development data with negative sentiment
fileNames = os.listdir(filePath + "dev/neg/")
negSentences = []
for i in range(1, len(fileNames)):
    file = open(filePath + "dev/neg/" + fileNames[i], 'r')
    negSentences.append(file.read())
print(len(negSentences))

# turn the assembled array of negative sentences into a pandas serries
negSeries = pd.Series(negSentences)

# obtain all instances of dev data with positive sentiment
fileNames = os.listdir(filePath + "dev/pos/")
posSentences = []
for i in range(1, len(fileNames)):
    file = open(filePath + "dev/pos/" + fileNames[i], 'r')
    posSentences.append(file.read())
print(len(posSentences))

# assembles everything into a Pandas dataframe
d = {'neg': pd.Series(negSentences), 'pos': pd.Series(posSentences)}
df = pd.DataFrame(d)
print(df.index)
print(df.columns)