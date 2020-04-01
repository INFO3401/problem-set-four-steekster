from utils import *
from pollingdata import *

import math
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt 

df = loadAndCleanData ("2020_democratic_presidential_nomination-6730.csv")

print(df)
normalizeData(df)

for candidate in df.columns:
	if candidate not in ["Spread", "Date", "Poll", "Sample", "Undecided"]:
		plotCandidate(candidate,df)


myCandidate = []
for candidate in df.columns:
	if candidate not in ["Spread", "Date", "Poll", "Sample"]:
		myCandidate.append(candidate)
		print(statsPerCandidate(candidate,df))

df = cleanSample(df)
print(df)

print(computePollWeight(df, "CNNCNN"))

print("Sanders: ", weightedStatsPerCandidate("Sanders", df))
print("Biden: ", weightedStatsPerCandidate("Biden", df))
print("Bloomberg: ", weightedStatsPerCandidate("Bloomberg", df))
print("Warren: ", weightedStatsPerCandidate("Warren", df))
print("Buttigieg: ", weightedStatsPerCandidate("Buttigieg", df))
print("Klobuchar: ", weightedStatsPerCandidate("Klobuchar", df))
print("Steyer: ", weightedStatsPerCandidate("Steyer", df))
print("Gabbard: ", weightedStatsPerCandidate("Gabbard", df))


repeatList = []
for candidate1 in myCandidate:
	for candidate2 in myCandidate:
		if candidate1 != candidate2:
			if [candidate1, candidate2] not in repeatList and [candidate1, candidate2] not in repeatList:
				print(candidate1,  "vs ", candidate2 , computeCorrelation(candidate1, candidate2, df))
				repeatList.append([candidate1, candidate2])
				
print("Biden and Klobuchar are the most correlated")
print("Sanders and Steyer are the least correlated")


superTuesday(df)
print("Biden Mean: ", df["BidenST"].mean())
print("Sanders Mean: ", df["SandersST"].mean())
print("Biden Weighted Mean: ", weightedStatsPerCandidate("BidenST", df))
print("Sanders Weighted Mean: ", weightedStatsPerCandidate("SandersST", df))



getConfidenceIntervals(df["BidenST"])
getConfidenceIntervals(df["SandersST"])


print("Numbers: ", runTTest(df["Biden"], df["Sanders"]))
print("Aggregated Numbers: ", runTTest(df["BidenST"], df["SandersST"]))
