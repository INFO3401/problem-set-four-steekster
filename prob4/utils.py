from scipy import stats

import pandas as pd

def loadAndCleanData(filename):
    data = pd.read_csv(filename, encoding='utf-8')
    data = data.dropna(axis=0)
    #print(data)
    return data

def computeProbability(feature, bin, data):
    count = 0
    for i,datapoint in data.iterrows():
        if datapoint[feature] >= bin[0] and datapoint[feature] < bin[1]:
            count += 1

    totalData = len(data)

    probability = count / totalData

    return probability

def getConfidenceIntervals(df):
    mean = df.mean()
    sigma = df.std()
    return stats.norm.interval(0.95, loc=mean, scale=sigma)

def runTTest(column1, column2):
    return stats.ttest_ind(column1, column2)