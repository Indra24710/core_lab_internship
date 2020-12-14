#importing the relevant packages
import pandas as pd

#reading the relevant csv files for the two categories, error and warning respectively
df=pd.read_csv('../Preprocessing/error.csv')
df1=pd.read_csv('../Preprocessing/warning.csv')


#classifying the data points into different categories based on error messages
syntax_error={}
syntax_error['id']=[]
syntax_error['error']=[]
syntax_error['error_type']=[]
syntax_error['name']=[]
syntax_error['time']=[]
syntax_error['memory']=[]
syntax_error['username']=[]

semantic_error={}
semantic_error['id']=[]
semantic_error['error']=[]
semantic_error['error_type']=[]
semantic_error['name']=[]   
semantic_error['time']=[]
semantic_error['memory']=[]
semantic_error['username']=[]

linker_error={}
linker_error['id']=[]
linker_error['error']=[]
linker_error['error_type']=[]
linker_error['name']=[]
linker_error['time']=[]         
linker_error['memory']=[]
linker_error['username']=[]

accepted={}
accepted['id']=[]
accepted['error']=[]
accepted['error_type']=[]
accepted['name']=[]
accepted['time']=[]
accepted['memory']=[]
accepted['username']=[]

runtime={}
runtime['id']=[]
runtime['error']=[]
runtime['error_type']=[]
runtime['name']=[]
runtime['time']=[]
runtime['memory']=[]
runtime['username']=[]

logical={}
logical['id']=[]
logical['error']=[]
logical['error_type']=[]
logical['name']=[]
logical['time']=[]
logical['memory']=[]
logical['username']=[]

unknown={}
unknown['id']=[]
unknown['error']=[]
unknown['error_type']=[]
unknown['name']=[]
unknown['time']=[]
unknown['memory']=[]
unknown['username']=[]



j=0
for i in df['error']:
    if 'expected' in i or 'stray' in i or 'illegal string constant' in i or 'not an l-value' in i or 'can\'t convert' in i:
        syntax_error['error'].append(i)
        syntax_error['id'].append(df['id'][j])
        syntax_error['error_type'].append(df['error_type'][j])
        syntax_error['memory'].append(df['memory'][j])
        syntax_error['time'].append(df['time'][j])
        syntax_error['username'].append(df['username'][j])
        syntax_error['name'].append(df['name'][j])

    if 'No such file or directory' in i:
        linker_error['error'].append(i)
        linker_error['id'].append(df['id'][j])
        linker_error['error_type'].append(df['error_type'][j])
        linker_error['memory'].append(df['memory'][j])
        linker_error['time'].append(df['time'][j])
        linker_error['username'].append(df['username'][j])
        linker_error['name'].append(df['name'][j])

    if 'undeclared' in i or 'too few arguments' in i or 'ld returned' in i or 'used uninitialized' in i or 'not supported' in i:
        semantic_error['error'].append(i)
        semantic_error['id'].append(df['id'][j])
        semantic_error['error_type'].append(df['error_type'][j])
        semantic_error['memory'].append(df['memory'][j])
        semantic_error['time'].append(df['time'][j])
        semantic_error['username'].append(df['username'][j])
        semantic_error['name'].append(df['name'][j]) 
    j+=1

j=0
flag=0

for i in df1['error']:
    if 'expected' in i or 'stray' in i or 'illegal string constant' in i or 'not an l-value' in i or 'can\'t convert' in i:
        syntax_error['error'].append(i)
        syntax_error['id'].append(df1['id'][j])
        syntax_error['error_type'].append(df1['error_type'][j])
        syntax_error['memory'].append(df1['memory'][j])
        syntax_error['time'].append(df1['time'][j])
        syntax_error['username'].append(df1['username'][j])
        syntax_error['name'].append(df1['name'][j])
        flag=1
    if 'No such file or directory' in i :
        linker_error['error'].append(i)
        linker_error['id'].append(df1['id'][j])
        linker_error['error_type'].append(df1['error_type'][j])
        linker_error['memory'].append(df1['memory'][j])
        linker_error['time'].append(df1['time'][j])
        linker_error['username'].append(df1['username'][j])
        linker_error['name'].append(df1['name'][j])
        flag=1

    if df1['error_type'][j]=='AC':
        accepted['error'].append(i)
        accepted['id'].append(df1['id'][j])
        accepted['error_type'].append(df1['error_type'][j])
        accepted['memory'].append(df1['memory'][j])
        accepted['time'].append(df1['time'][j])
        accepted['username'].append(df1['username'][j])
        accepted['name'].append(df1['name'][j])
        flag=1

    if df1['error_type'][j]=='RTE' or df1['error_type'][j]=='TLE' or df1['error_type'][j]=='MLE'or df1['error_type'][j]=='OLE':
        runtime['error'].append(i)
        runtime['id'].append(df1['id'][j])
        runtime['error_type'].append(df1['error_type'][j])
        runtime['memory'].append(df1['memory'][j])
        runtime['time'].append(df1['time'][j])
        runtime['username'].append(df1['username'][j])
        runtime['name'].append(df1['name'][j])
        flag=1

    if df1['error_type'][j]=='WA':
        logical['error'].append(i)
        logical['id'].append(df1['id'][j])
        logical['error_type'].append(df1['error_type'][j])
        logical['memory'].append(df1['memory'][j])
        logical['time'].append(df1['time'][j])
        logical['username'].append(df1['username'][j])
        logical['name'].append(df1['name'][j])
        flag=1
    
    if 'undeclared' in i or 'too few arguments' in i or 'ld returned' in i or 'used uninitialized' in i or 'not supported' in i:
        semantic_error['error'].append(i)
        semantic_error['id'].append(df1['id'][j])
        semantic_error['error_type'].append(df1['error_type'][j])
        semantic_error['memory'].append(df1['memory'][j])
        semantic_error['time'].append(df1['time'][j])
        semantic_error['username'].append(df1['username'][j])
        semantic_error['name'].append(df1['name'][j])
        flag=1
    
    if flag==0:
        unknown['error'].append(i)
        unknown['id'].append(df1['id'][j])
        unknown['error_type'].append(df1['error_type'][j])
        unknown['memory'].append(df1['memory'][j])
        unknown['time'].append(df1['time'][j])
        unknown['username'].append(df1['username'][j])
        unknown['name'].append(df1['name'][j])

    flag=0 



         
    j+=1

df1=pd.read_csv('../Preprocessing/unknown.csv')
j=0
flag=0
for i in df1['error']:
    if 'expected' in i or 'illegal string constant' in i or 'not an l-value' in i or 'can\'t convert' in i or 'stray' in i:
        syntax_error['error'].append(i)
        syntax_error['id'].append(df1['id'][j])
        syntax_error['error_type'].append(df1['error_type'][j])
        syntax_error['memory'].append(df1['memory'][j])
        syntax_error['time'].append(df1['time'][j])
        syntax_error['username'].append(df1['username'][j])
        syntax_error['name'].append(df1['name'][j])
        flag=1
    if 'No such file or directory' in i :
        linker_error['error'].append(i)
        linker_error['id'].append(df1['id'][j])
        linker_error['error_type'].append(df1['error_type'][j])
        linker_error['memory'].append(df1['memory'][j])
        linker_error['time'].append(df1['time'][j])
        linker_error['username'].append(df1['username'][j])
        linker_error['name'].append(df1['name'][j])
        flag=1

    if df1['error_type'][j]=='AC':
        accepted['error'].append(i)
        accepted['id'].append(df1['id'][j])
        accepted['error_type'].append(df1['error_type'][j])
        accepted['memory'].append(df1['memory'][j])
        accepted['time'].append(df1['time'][j])
        accepted['username'].append(df1['username'][j])
        accepted['name'].append(df1['name'][j])
        flag=1

    if df1['error_type'][j]=='RTE' or df1['error_type'][j]=='TLE' or df1['error_type'][j]=='MLE'or df1['error_type'][j]=='OLE':
        runtime['error'].append(i)
        runtime['id'].append(df1['id'][j])
        runtime['error_type'].append(df1['error_type'][j])
        runtime['memory'].append(df1['memory'][j])
        runtime['time'].append(df1['time'][j])
        runtime['username'].append(df1['username'][j])
        runtime['name'].append(df1['name'][j])
        flag=1

    if df1['error_type'][j]=='WA':
        logical['error'].append(i)
        logical['id'].append(df1['id'][j])
        logical['error_type'].append(df1['error_type'][j])
        logical['memory'].append(df1['memory'][j])
        logical['time'].append(df1['time'][j])
        logical['username'].append(df1['username'][j])
        logical['name'].append(df1['name'][j])
        flag=1
    
    if 'undeclared identifier' in i or 'too few arguments' in i or 'ld returned' in i or 'used uninitialized' in i or 'not supported' in i:
        semantic_error['error'].append(i)
        semantic_error['id'].append(df1['id'][j])
        semantic_error['error_type'].append(df1['error_type'][j])
        semantic_error['memory'].append(df1['memory'][j])
        semantic_error['time'].append(df1['time'][j])
        semantic_error['username'].append(df1['username'][j])
        semantic_error['name'].append(df1['name'][j])
        flag=1

    if flag==0:
        unknown['error'].append(i)
        unknown['id'].append(df1['id'][j])
        unknown['error_type'].append(df1['error_type'][j])
        unknown['memory'].append(df1['memory'][j])
        unknown['time'].append(df1['time'][j])
        unknown['username'].append(df1['username'][j])
        unknown['name'].append(df1['name'][j])
    flag=0 


         
    j+=1








#print(len(syntax_error['error']))
syntax_error=pd.DataFrame.from_dict(syntax_error)
semantic_error=pd.DataFrame.from_dict(semantic_error)
linker_error=pd.DataFrame.from_dict(linker_error)
logical=pd.DataFrame.from_dict(logical)
runtime=pd.DataFrame.from_dict(runtime)
accepted=pd.DataFrame.from_dict(accepted)
unknown=pd.DataFrame.from_dict(unknown)

#print(syntax_error.head)
print(semantic_error.head)
syntax_error.to_csv('syntax_error.csv',index=False)
semantic_error.to_csv('semantic_error.csv',index=False)
linker_error.to_csv('linker_error.csv',index=False)
logical.to_csv('logical.csv',index=False)
runtime.to_csv('runtime.csv',index=False)
accepted.to_csv('accepted.csv',index=False)
unknown.to_csv('unknown_class.csv',index=False)
