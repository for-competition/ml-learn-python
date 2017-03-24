# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:56:14 2017

@author: zackery
"""
import pandas as pd

data = pd.read_csv('F:/forecast/data1/total_20170225.csv',sep='\t')
data=list(data.iloc[:,1])
ts=list(reversed(data))

'差分函数'
def diff(ts,n):
    i = 0
    ts_diff=[]
    for i in range(len(ts)-n-1):
        ts[i]=ts[i]-ts[i+n]
        ts_diff.append(ts[i])
    return ts_diff
 
'预测未来一天'    
def forecast_sarima(ts):
    tst=tuple(ts)
    ar = [0.12541177,-0.14934047,0.04358712,0.06999451,-0.01438823,0.18472227, -0.36614783 ]
    sar= [-0.31689317]
    diff_none=list(tst)
    diff_list = diff(list(tst),1)
    diff_seasonal = diff(diff(list(tst),1),len(ar))
    phi=0
    for i in range(len(ar)):
        ds=diff_seasonal[i:i+len(sar)*len(ar)+1:len(ar)]
        seasonal_phi=diff_seasonal[i]-sum(map(lambda x,y:x*y,sar,ds[1:]))
        phi=phi+ar[i]*seasonal_phi
    phi=phi+sum(map(lambda x,y:x*y,sar,diff_seasonal[len(ar)-1:len(ar)-1+len(sar)])) 
    return phi+diff_list[len(ar)-1]+diff_none[0]
 
'预测N天'    
def forecast_days(ts,n):
    forecast_series=[]
    for i in range(n):
        result=forecast_sarima(ts)
        forecast_series.append(result)
        ts.insert(0,result)
    return forecast_series

