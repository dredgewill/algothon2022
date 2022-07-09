import numpy as np
import pandas as pd
from scipy import stats as st

nInst=100
currentPos = np.zeros(nInst)

def getMyPosition (prcSoFar):
    global currentPos
    for x in range(100):
        if prcSoFar[0].size < 30:
            return currentPos
        currentPos[x] = st.zscore(prcSoFar[x])[-1]
        if np.isnan(currentPos[x] or currentPos[x] < 3):
            currentPos[x] = 0
        else:
            currentPos[x] = round(currentPos[x]*100)
    return currentPos