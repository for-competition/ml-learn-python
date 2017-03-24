# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 16:04:03 2017
@author:zackery 
"""
import pandas as pd


dingdan=pd.read_csv('F:/dingdan.csv')
col_names=['ID','create_time','service_order_id']
dingdan.columns = col_names
dingdan.head(5)
'''dingdan=dingdan.set_index('ID')['create_time'].to_dict()'''

mydict = {}
for x in range(len(dingdan)):
    currentid = dingdan.iloc[x,0]
    currentvalue = dingdan.iloc[x,1]
    mydict.setdefault(currentid,[])
    mydict[currentid].append(currentvalue)
    
'''mydict={k: g["value"].tolist() for k,g in dingdan.groupby("id")}''' 
    

def list_num(a):
    isinstance(a,list)
    a.sort(reverse=True)
    b=[]
    for i in range(len(a)-1):
        if a[i] - a[i+1] > 900:
            b.append(a[i])
        else:
            continue
    return(len(b)+1)
    
def count_dingdan(a):
    isinstance(a,dict)
    b=0
    for key in a:
        b+=a[key]
    return b

       
newdict={}
for key in mydict:
    num=list_num(mydict[key])
    dic={key:num}
    newdict.update(dic)
count_dingdan(newdict)   
 

    
        
    
    
    
    
    