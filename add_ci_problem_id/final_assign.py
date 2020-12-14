import json
import pandas as pd

f=open('final_prob_id.json')
f=json.load(f)
df=pd.read_csv('finetuned.csv')
f2=open('prolemid-submissionid.json')
f2=json.load(f2)

id_problem_id={}
for i in f.keys():
    id_problem_id[i]=f[i]

for i in f2:
    if i['problem_id']!=None:
        id_problem_id[i['id']]=i['problem_id']

li=[]
count=0
for i in df['id']:
    if str(i) in id_problem_id.keys():
        li.append(id_problem_id[str(i)])
        count+=1
        # print(count)
    else:
        li.append(0)

df['problem_id']=li
df.to_csv('final_data.csv',index=False)
df_temp=df[df['problem_id']!=0]
print(len(df_temp))
