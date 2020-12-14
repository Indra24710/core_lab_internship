import json
import pandas as pd
import os
f=open('submission_code.json')
f=json.load(f)
df=pd.read_csv('finetuned_new.csv')
c_programs=[]
for i in range(len(df['id'])):
    if df['name'][i]=='C':
        c_programs.append(df['id'][i])


filename=''
count=0
for i in f:
    if int(i['id']) in c_programs:
        print(count)
        count+=1
        try:
            filename=open(os.path.join('program_codes/'+i['id']+'.c'),'w')
            filename.write(i['source'])
        except:
            continue

