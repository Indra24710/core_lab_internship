import os
import numpy as np
import json
import pandas as pd



df1=pd.read_csv('finetuned.csv')
df1['date']=pd.to_datetime(df1['date'])

df1['index']=[i for i in range(len(df1))]
req_usernames=list(set(df1[df1['error_type']=='CI']['username']))

# print(type(df1['date'][0]))

req_ids={}

for i in req_usernames:
    req_ids[i]=list(df1[(df1['username']==i)&(df1['error_type']=='CI')]['index'])
# print(len(df1[df1['error_type']=='CI']))
req_json={}
count=0
for i in req_ids.keys():
    req_json[i]={}
    for j in req_ids[i]:
        req_json[i][str(df1['id'][j])]=[]
        df_temp=df1[(df1['username']==i)&(df1['error_type']!='CI')]
        for k in df_temp['index']:
            if df_temp['date'][k].day==df1['date'][j].day and df_temp['date'][k].hour <= df1['date'][j].hour:
                req_json[i][str(df1['id'][j])].append(str(df_temp['id'][k]))
        # print(req_json[i][df1['id'][j]])
        print(count)
        count+=1

f=open('req_json.json','w')
json.dump(req_json,f)









