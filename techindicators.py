import numpy as np
#
# Simple Moving Average
# a is an array of prices, b is a period for averaging
def sma(a,b):
    result = np.zeros(len(a)-b+1)
    for i in range(len(a)-b+1):
        result[i] = np.sum(a[i:i+b])/b
    return result
#
# Exponential Moving Average
# a is an array of prices, b is a period for averaging
def ema(a,b):
    result = np.zeros(len(a)-b+1)
    result[0] = np.sum(a[0:b])/b
    for i in range(1,len(result)):
        result[i] = result[i-1]+(a[i+b-1]-result[i-1])*(2/(b+1))
    return result
#
# Kaufman's Adaptive Moving Average
# a is an array of prices, b is the period for the efficiency ratio
# c is the period for the fast EMA, d is the period for the slow EMA
def kama(a,b,c,d):
    fsc = 2/(c+1)# fast smoothing constant
    ssc = 2/(d+1)# slow smoothing constant
    er = np.zeros(len(a))# efficiency ratio
    pv = np.zeros(len(a))# periodic volatility
    pd = np.zeros(len(a))# price direction
    for i in range(1,len(a)):
        pv[i] = np.fabs(a[i]-a[i-1])
    for i in range(b,len(a)):
        pd[i] = np.fabs(a[i]-a[i-b])
    for i in range(b,len(a)):
        er[i] = pd[i]/np.sum(pv[i-b+1:i+1])
    sc = (er*(fsc-ssc)+ssc)**2
    result = np.zeros(len(a))
    result[b-1] = a[b-1]
    for i in range(b,len(a)):
        result[i] = result[i-1]+sc[i]*(a[i]-result[i-1])
    return result[b-1:]
#
# Average True Range
# a is array of high prices, b is array of low prices, 
# c is array of closing prices, d is period for averaging
def atr(a,b,c,d):
    tr = np.zeros(len(a))
    result = np.zeros(len(a)-d+1)
    tr[0] = a[0]-b[0]
    for i in range(1,len(a)):
        hl = a[i]-b[i]
        hpc = np.fabs(a[i]-c[i-1])
        lpc = np.fabs(b[i]-c[i-1])
        tr[i] = np.amax(np.array([hl,hpc,lpc]))
    print(tr)
    result[0] = np.sum(tr[0:d])/d
    for i in range(1,len(a)-d+1):
        result[i] = (result[i-1]*(d-1)+tr[i+d-1])/d
    return result

