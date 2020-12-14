import pandas as pd

df=pd.read_csv('semantic_error.csv')

df['Undeclared identifiers']=0
df['Argument error']=0
df['Typographical error']=0
df['Uninitialized characters']=0
df['Unsupported type errors']=0


j=0
for i in df['error']:

    if 'undeclared identifier' in i:
        df['Undeclared identifiers'][j]=1 

    if 'too few arguments' in i:
        df['Argument error'][j]=1

    if 'ld returned' in i:
        df['Typographical error'][j]=1 

    if 'used uninitialized' in i:
        df['Uninitialized characters'][j]=1

    if 'not supported' in i:
        df['Unsupported type errors'][j]=1

    j+=1

print(df.head)
df.to_csv('semantic_error.csv',index=False)
