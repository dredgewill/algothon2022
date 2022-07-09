import numpy as np
import pandas as pd
import statistics
from scipy import stats as st

nInst=100
currentPos = np.zeros(nInst)

def getMyPosition (prcSoFar):
    global currentPos
    if prcSoFar[0].size >= 5:
        for x in range(100):
            growth = []
            for i in range(1,5):
                growth.append(prcSoFar[x][-i]/prcSoFar[x][-i-1]-1)
            if abs(statistics.mean(growth)) > 0.01 and statistics.stdev(growth) < 0.005:
                currentPos[x] = statistics.mean(growth) * 100000
    if 0:
        for x in range(100):
            if prcSoFar[0].size < 30:
                return currentPos
            currentPos[x] = st.zscore(prcSoFar[x])[-1]
            if np.isnan(currentPos[x] or currentPos[x] < 3):
                currentPos[x] = 0
            else:
                currentPos[x] = round(currentPos[x]*100)
    return currentPos