import pandas as pd

df=pd.read_csv('syntax_error.csv')

df['Missing characters']=0
df['L-value errors']=0
df['illegal string constant']=0
df['Stray characters']=0

j=0
for i in df['error']:

    if 'expected' in i:
        df['Missing characters'][j]=1

    if 'illegal' in i:
        df['illegal string constant'][j]=1
    
    if 'stray' in i:
        df['Stray characters'][j]=1
    
    if 'not an l-value' in i:
        df['L-value errors'][j]=1
    
    j+=1

print(df.head)
df.to_csv('syntax_error.csv',index=False)
