# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 16:04:03 2017
@author:zackery 
"""

"""
sqlContext=('select
                   cast(a.user_id as varchar(10))  id,
                   cast(a.create_time as varchar(10))  create_time,
                   a.status  status
               from(
                    select
                          user_id,
                          create_time,
                          status,
                          row_number() over(partition by service_order_id order by update_time desc) num
                      from
                          ods_service_order
                      where dt>20161231
                        and end_time>=unix_timestamp('2017-01-01 00:00:00')
                        and end_time<unix_timestamp('2017-01-02 00:00:00')
             ) as a
             where a.num=1
')
"""

               
import pandas as pd


def data_read(locate):
    dingdan=pd.read_csv(locate)
    col_names=['ID','create_time','status']
    dingdan.columns = col_names
    return dingdan
    
    
'''dingdan.head(5)'''
'''dingdan=dingdan.set_index('ID')['create_time'].to_dict()'''

def sheet2dict(dingdan):
    mydict = {}
    for x in range(len(dingdan)):
        currentid = dingdan.iloc[x,0]
        currentvalue = {dingdan.iloc[x,1]:dingdan.iloc[x,2]}
        mydict.setdefault(currentid,{})
        mydict[currentid].update(currentvalue)
    return mydict
    
'''mydict={k: g["value"].tolist() for k,g in dingdan.groupby("id")}''' 
    

def list_num(a):
    isinstance(a,dict)
    a0=sorted(a.keys(),reverse=True)
    b=[]
    for i in range(len(a0)-1):
        if a0[i] - a0[i+1] > 900:
            b.append(a0[i])
        elif a0[i] - a0[i+1] <= 900 and a[a0[i]] == 7:
            b.append(a0[i])
        else:
            continue
    return(len(b)+1)

    
def count_dingdan(a):
    isinstance(a,dict)
    b=0
    for key in a:
        b+=a[key]
    return b

       
    
mydict=sheet2dict(data_read(raw_input()))
newdict={}
for key in mydict:
    num=list_num(mydict[key])
    dic={key:num}
    newdict.update(dic)
count_dingdan(newdict)   
 

    
        
    
    
    
    
    