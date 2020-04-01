import matplotlib.pyplot as plt 
import numpy as np


def normalizeData(df):
	x = df.copy()
	sumList = []

	for i, row in x.iterrows():
		row.drop(labels = ["Poll", "Date", "Sample", "Spread"], inplace = True)
		print(row) 
		sumList.append(100-sum(row))

	x["Undecided"] = sumList

	print(x)

def plotCandidate(candidate,df):
	plt.scatter(y = df[candidate], x=df["Poll"]) #variables no quotes
	plt.title(candidate + "Polling")
	plt.ylim(0) # so the bottom is 0
	plt.show()


def statsPerCandidate(candidate,df):
		return df[candidate].mean()


def cleanSample(df):
	sampleType = []
	sampleSize = []
	for i, row in df.iterrows():
		if "RV" in row["Sample"]:
			sampleType.append("RV")
			sampleSize.append(row["Sample"].replace(" RV", ""))
		elif "LV" in row["Sample"]:
			sampleType.append("LV")
			sampleSize.append(row["Sample"].replace(" LV", ""))
	for size in range(len(sampleSize)):
		if "RV" not in sampleSize[size] and "LV" not in sampleSize[size]: int(sampleSize[size])
		else:sampleSize[size] = 0
	df["Sample Type"] = sampleType
	df["Sample Size"] = sampleSize

	return df


def computePollWeight(data, Poll):
    pollsum = 0
    for i,v in data.iterrows():
        if v[0] == Poll:
            pollsum += int(v[9])

    weight = pollsum / data['Sample Size'].astype(int).sum()
    return weight


def weightedStatsPerCandidate(candidate,df):
	weightedAverages = []
	for poll in df["Poll"].unique():
		x = sum(df[df["Poll"] == poll][candidate])
		y = computePollWeight(df, poll)
		weightedAverages.append(x*y)
	return sum(weightedAverages)/len(weightedAverages)

def computeCorrelation(candidate1, candidate2, dataframe):
    return np.corrcoef(dataframe[candidate1], dataframe[candidate2])[0][1]


def superTuesday(dataframe):
    candidates = ['Bloomberg', 'Warren', 'Klobuchar', 'Buttigieg', 'Steyer']
    
    dataframe['SandersST'] = dataframe['Sanders']
    dataframe['BidenST'] = dataframe['Biden']

    for i in candidates:
        bern = computeCorrelation('Sanders', i, dataframe)
        joe = computeCorrelation('Biden', i, dataframe)

        if bern > joe:
            dataframe['SandersST'] = dataframe['SandersST'] + dataframe[i]
        elif joe > bern:
            dataframe['BidenST'] = dataframe['BidenST'] + dataframe[i]

    return dataframe











