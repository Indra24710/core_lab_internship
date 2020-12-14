#extract error message from html error string
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    text=re.sub(clean, '', text)
    return re.sub('\s+', ' ', text)

#import relevant packages
import json
import pandas as pd
import matplotlib.pyplot as plt

#loading the data
f=open('judge_submission.json')
error_data=json.load(f)


#extracting C language based data-points from the complete dataset 
unprocessed_data={}
unprocessed_data['id']=[]
unprocessed_data['error']=[]
unprocessed_data['error_type']=[]
unprocessed_data['name']=[]
unprocessed_data['time']=[]
unprocessed_data['memory']=[]
unprocessed_data['username']=[]
count=0
for i in error_data:
    if i['name']=='C' and i['result']!=None:
        unprocessed_data['id'].append(i['id'])
        if i['error']==None:
            unprocessed_data['error'].append('No error')
        else:
            unprocessed_data['error'].append(i['error'])
        unprocessed_data['error_type'].append(i['result'])
        unprocessed_data['name'].append(i['name'])
        if i['time']==None:
            unprocessed_data['time'].append(0)
        else:
            unprocessed_data['time'].append(i['time'])
        if i['time']==None:
            unprocessed_data['memory'].append(0)
        else:
            unprocessed_data['memory'].append(i['memory'])
        unprocessed_data['username'].append(i['username'])


#processing the data using the remove_html_tags function

processed_data={}
processed_data['id']=[]
processed_data['error']=[]
processed_data['error_type']=[]
processed_data['name']=[]
processed_data['time']=[]
processed_data['memory']=[]
processed_data['username']=[]

error={}
error['id']=[]
error['error']=[]
error['error_type']=[]
error['name']=[]
error['time']=[]
error['memory']=[]
error['username']=[]

warning={}
warning['id']=[]
warning['error']=[]
warning['error_type']=[]
warning['name']=[]
warning['time']=[]
warning['memory']=[]
warning['username']=[]

unknown={}
unknown['id']=[]
unknown['error']=[]
unknown['error_type']=[]
unknown['name']=[]
unknown['time']=[]
unknown['memory']=[]
unknown['username']=[]




for i in range(len(unprocessed_data['error'])):
    s=remove_html_tags(unprocessed_data['error'][i])
    s=s.replace('\n',' ').split('error: ')
    if len(s)>1:
        temp=' '
        pos=0
        for j in s:
            if pos==0:
                pos=1
                pass
            else:
                temp+=j
        processed_data['error'].append('error: '+temp)
        error['error'].append(temp)
        error['id'].append(unprocessed_data['id'][i])
        error['error_type'].append(unprocessed_data['error_type'][i])
        error['memory'].append(unprocessed_data['memory'][i])
        error['time'].append(unprocessed_data['time'][i])
        error['username'].append(unprocessed_data['username'][i])
        error['name'].append(unprocessed_data['name'][i])
    else:
        s=s[0]
        s=s.split('warning: ')
        if len(s)>1:
            pos=0
            temp=' '
            for j in s:
                if pos==0:
                    pos=1
                    pass
                else:
                    temp+=j
            processed_data['error'].append('warning: '+temp)
            warning['error'].append(temp)
            warning['id'].append(unprocessed_data['id'][i])
            warning['error_type'].append(unprocessed_data['error_type'][i])
            warning['memory'].append(unprocessed_data['memory'][i])
            warning['time'].append(unprocessed_data['time'][i])
            warning['username'].append(unprocessed_data['username'][i])
            warning['name'].append(unprocessed_data['name'][i])
            
        else:
            processed_data['error'].append(s[0])
            unknown['error'].append(temp)
            unknown['id'].append(unprocessed_data['id'][i])
            unknown['error_type'].append(unprocessed_data['error_type'][i])
            unknown['memory'].append(unprocessed_data['memory'][i])
            unknown['time'].append(unprocessed_data['time'][i])
            unknown['username'].append(unprocessed_data['username'][i])
            unknown['name'].append(unprocessed_data['name'][i])
    processed_data['id'].append(unprocessed_data['id'][i])
    processed_data['error_type'].append(unprocessed_data['error_type'][i])
    processed_data['memory'].append(unprocessed_data['memory'][i])
    processed_data['time'].append(unprocessed_data['time'][i])
    processed_data['username'].append(unprocessed_data['username'][i])
    processed_data['name'].append(unprocessed_data['name'][i])

#the complete processed data
df=pd.DataFrame.from_dict(processed_data)
df.to_csv('processed_data.csv',index=False)

#data points of submissions with error
df1=pd.DataFrame.from_dict(error)
df1.to_csv('error.csv',index=False)

#data points of submissions with warning
df2=pd.DataFrame.from_dict(warning)
df2.to_csv('warning.csv',index=False)

#data points of submissions that does not fall in either of the above categories.
df3=pd.DataFrame.from_dict(unknown)
df3.to_csv('unknown.csv',index=False)