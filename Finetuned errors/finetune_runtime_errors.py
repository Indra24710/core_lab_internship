import pandas as pd

df=pd.read_csv('runtime.csv')

df['Time limit exceeded']=0
df['Memory limit exceeded']=0
df['Object Linking errors']=0
df['Other Runtime errors']=0

j=0
for i in df['error_type']:

    if i=='TLE':
        df['Time limit exceeded']=0

    if i=='MLE':
        df['Memory limit exceeded']=0
    
    if i=='OLE':
        df['Object Linking errors']=0
    
    if i=='RTE':
        df['Other Runtime errors']=0
    
    j+=1

print(df.head)
df.to_csv('runtime.csv',index=False)
