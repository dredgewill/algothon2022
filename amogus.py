import numpy as np
import pandas as pd
import statistics
from scipy import stats as st

nInst=100
currentPos = np.zeros(nInst)
grate = 0.01
grate_zscore_multi = 0.2
PosMulti = 12
GrowthRangeMax = 3
HISTSIZE = GrowthRangeMax + 1
zscore_min = 1.5

def getMyPosition (prcSoFar):
    global currentPos
    """
    if prcSoFar[0].size >= 101:
        for x in range(100):
            growth = []
            for i in range(1,5):
                growth.append(prcSoFar[x][-i]/prcSoFar[x][-i-1]-1)
            if abs(statistics.mean(growth)) > grate and statistics.stdev(growth) < 0.005:
                currentPos[x] = statistics.mean(growth) * 100000
    if prcSoFar[0].size <= HISTSIZE:
        return currentPos
    for x in range(100):
        zdev = st.zscore(prcSoFar[x])[-1]
        if np.isnan(zdev):
            currentPos[x] = 0
        else:
            growth = []
            for i in range(1,GrowthRangeMax):
                growth.append(prcSoFar[x][-i]/prcSoFar[x][-i-1]-1)
            if statistics.stdev(growth) < grate * grate_zscore_multi and abs(zdev) > zscore_min:
                if (abs(statistics.mean(growth)) > grate and np.sign(zdev) == np.sign(statistics.mean(growth))):
                    currentPos[x] = round(statistics.mean(growth) * 100 * PosMulti * abs(zdev))
    """
    return [-10000]*100