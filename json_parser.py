# -*- coding: utf-8 -*-
"""
@zackery
"""
import csv
import json

 
def json_parser(a,f):
   for key in a:
       f.write(str(key)+',')
       if isinstance(a[key],dict):
           f.write('\n')
           json_parser(a[key],f)
       else:
           f.write(str(a[key])+'\n')
           

def json_parser_key(a,f):
   for key in a:
       f.write(str(key)+',')
       if isinstance(a[key],dict):
           f.write('\n')
           json_parser_key(a[key],f)
           
           
           
driver_change=open('F:/driver_change.csv','r')
driver_change_result=open('F:/driver_change_result.csv','w')
reader = csv.reader((line.replace('\0','') for line in driver_change),delimiter=",")
for row in reader:       
    for m in row[:7]:       
        driver_change_result.write(str(m)+',')
    for n in row[9:12]:
        driver_change_result.write(str(n)+',')
    dc_json=json.loads(row[8])
    json_parser(dc_json,driver_change_result)
driver_change_result.close()
driver_change.close()
    

for row in reader:
    dc_json=json.loads(row[8])
    json_parser_key(dc_json,driver_change_result)        
