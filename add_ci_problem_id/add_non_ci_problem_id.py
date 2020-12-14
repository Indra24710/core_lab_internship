import pandas as pd
import json

df=pd.read_csv('finetuned_new.csv')
f=open('prolemid-submissionid.json')
f=json.load(f)

problem_id={}
for i in f:
    if i['problem_id']!=None:
        problem_id[i['id']]=i['problem_id']

li=[]
for i in df['id']:
    if str(i) not in problem_id.keys():
        li.append('0')
    else:
        li.append(problem_id[str(i)])

df['problem_id']=li
df.to_csv('finetuned.csv',index=False)