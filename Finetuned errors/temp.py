import pandas as pd
df=pd.read_csv('finetuned.csv')
print(len(df),len(list(set(df['id']))))