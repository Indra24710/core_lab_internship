import json
import pandas as pd

df=pd.read_csv('finetuned.csv')
li={}
f=open('judge_submission.json')
f=json.load(f)
for i in f:
    li[i['id']]=i['date']

date=[]
for i in df['id']:
    date.append(li[str(i)])
df['date']=pd.to_datetime(date)
df=df.sort_values(by='date')
df.to_csv('finetuned_new.csv',index=False)
print(df.info())