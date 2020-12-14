import pandas as pd

preprocessed=pd.read_csv('../Preprocessing/processed_data.csv')
errors=pd.read_csv('../Preprocessing/error.csv')
warning=pd.read_csv('../Preprocessing/warning.csv')
unknown=pd.read_csv('../Preprocessing/unknown.csv')


# finetuning the data points by further segregating the error categories into corresponding error messages
preprocessed.dropna(inplace=True)
finetuned={}
finetuned={}
finetuned['id']=[]
finetuned['error_type']=[]
finetuned['name']=[]
finetuned['time']=[]
finetuned['memory']=[]
finetuned['username']=[]


#runtime errors
finetuned['Time limit exceeded']=[]
finetuned['Memory limit exceeded']=[]
finetuned['Object Linking errors']=[]
finetuned['other runtime errors']=[]


#semantic errors
finetuned['Undeclared identifiers']=[]
finetuned['Argument error']=[]
finetuned['Typographical error']=[]
finetuned['uninitialized variables']=[]
finetuned['Incompatible type errors']=[]


#linker erros
finetuned['Linker error']=[]

#logical errors
finetuned['logical error']=[]

#syntax errors
finetuned['stray characters']=[]
finetuned['l-value error']=[]
finetuned['programming language error']=[]

finetuned['accepted']=[]

l=len(preprocessed['error'])
char_list=[' \'=\' ',' \',\' ',' \';\' ',' \')\' ',' \'(\' ',' \'{\' ',' \'}\' ',' \'.\' ',' \'[\' ',' \']\' ']
char_list_count={}

for i in range(l):
    if preprocessed['error'][i]!=None:
        for j in char_list:
            if j in char_list_count.keys():
                char_list_count[j].append(0)
            else:
                char_list_count[j]=[0]

for i in char_list_count.keys():
    finetuned['missing '+i]=char_list_count[i]


j=0
for i in preprocessed['error']:
    if i!=None:
        finetuned['id'].append(preprocessed['id'][j])
        finetuned['error_type'].append(preprocessed['error_type'][j])
        finetuned['name'].append(preprocessed['name'][j])
        finetuned['time'].append(preprocessed['time'][j])
        finetuned['memory'].append(preprocessed['memory'][j])
        finetuned['username'].append(preprocessed['username'][j])

        #runtime errors
        if preprocessed['error_type'][j]=='TLE':
            finetuned['Time limit exceeded'].append(1)
        else:
            finetuned['Time limit exceeded'].append(0)

        if preprocessed['error_type'][j]=='MLE':
            finetuned['Memory limit exceeded'].append(1)
        else:
            finetuned['Memory limit exceeded'].append(0)

        if preprocessed['error_type'][j]=='OLE':
            finetuned['Object Linking errors'].append(1)
        else:
            finetuned['Object Linking errors'].append(0)

        if preprocessed['error_type'][j]=='RTE':
            finetuned['other runtime errors'].append(1)
        else:
            finetuned['other runtime errors'].append(0)

        #semantic errors
        
        if 'undeclared' in i:
            finetuned['Undeclared identifiers'].append(i.count('undeclared'))
        else:
            finetuned['Undeclared identifiers'].append(0)
        
        if 'expects argument' in i:
            finetuned['Argument error'].append(i.count('expects argument'))
        else:
            finetuned['Argument error'].append(0)

        if 'ld returned' in i:
            finetuned['Typographical error'].append(i.count('ld returned'))
        else:
            finetuned['Typographical error'].append(0)
        
        if 'uninitialized' in i:
            finetuned['uninitialized variables'].append(i.count('uninitialized'))
        else:
            finetuned['uninitialized variables'].append(0)  

        if 'incompatible' in i:
            finetuned['Incompatible type errors'].append(i.count('incompatible'))
        else:
            finetuned['Incompatible type errors'].append(0)

        #Linker error

        if 'No such file or directory' in i:
            finetuned['Linker error'].append(i.count('No such file or directory'))
        else:
            finetuned['Linker error'].append(0)

        #logical errors

        if preprocessed['error_type'][j]=='WA':
            finetuned['logical error'].append(1)
        else:
            finetuned['logical error'].append(0)
        
        #accepted
        if preprocessed['error_type'][j]=='AC':
            finetuned['accepted'].append(1)
        else:
            finetuned['accepted'].append(0)

        #syntax error

        for k in char_list:
            finetuned['missing '+k][j]= i.count(k)
        
        if 'stray' in i:
            finetuned['stray characters'].append(i.count('stray'))
        else:
            finetuned['stray characters'].append(0)
        
        if 'java' in i or 'python' in i or 'import' in i:
            finetuned['programming language error'].append(1)
        else:
            finetuned['programming language error'].append(0)

        if  'not an l-value' in i:
            finetuned['l-value error'].append(i.count('not an l-value'))
        else:
            finetuned['l-value error'].append(0)
    
    j+=1


# df=pd.DataFrame.from_dict(finetuned)
# df.to_csv('finetuned.csv',index=False)
# print(df.head)

print(len(finetuned['id']),len(list(set(finetuned['id']))))






      





      




         
