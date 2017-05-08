# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 13:59:01 2017

@author: zackery
"""
import csv

#划分区块
lat = 39.6
lng = 116.1
block = {}
i = 0
while lat <= 40.2:
     while lng <= 116.74:
         value = {'latitude':[lat,round(lat+0.02,2)],'longitude':[lng,round(lng+0.02,2)] }
         lng = round(lng + 0.02,2)
         block.setdefault(i,{})
         block[i].update(value)
         i+=1
     lat = round(lat +0.02,2)
     lng = 116.1
block     

#判断属于哪个block
def which_one(lat,lng):
    wo = -1
    for i in range(1023):
        if (lat > block[i]['latitude'][0] and lat < block[i]['latitude'][1]) and (lng > block[i]['longitude'][0] and lat < block[i]['longitude'][1]):
           wo = i
           break
    return wo


with open('F:/result.csv','w',newline='') as final:
    writer = csv.writer(final)
    try:    
        with open ('F:/order.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    index=which_one(float(row[3]),float(row[4]))
                    row.append(index)
                    writer.writerow(row)
                except:
                    print('write error')
    except:
        print('read,error')
    finally:
        final.close()
             
 
'''
select
from_unixtime(b.end_time,'yyyy-MM-dd') dates,
from_unixtime(b.end_time,'HH') hour,
b.service_order_id,
b.start_latitude,
b.start_longitude
from (
  select
  a.service_order_id,
  a.start_latitude,
  a.start_longitude,
  a.end_time
  from yc_bit.ods_service_order a
  where a.dt>=20160915
  and a.city='bj'
  ) as b
where 
b.end_time>=unix_timestamp('2016-09-15 00:00:00')
and b.end_time<=unix_timestamp('2016-12-31 00:00:00')
and start_latitude>=39.6
and start_latitude<=40.2
and start_longitude>=116.1
and start_longitude<=116.75
'''


'''
CREATE TABLE `yc_tmp.zhigangtest`(
day string,
hour string,
id string,
lat string,
lon string,
index string
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','

load  data  local inpath  'yuyin.csv' into table yc_tmp.zhigangtest; 
'''





















        