import pandas as pd
import os

# create a dataframe
data={
  'Name':['Alice','Bob','Charlie'],
  'age':[25,30,35],
  'city':['New york','Los Angeles' ,'Chicago']
}

df=pd.DataFrame(data)

""" #Adding new row to df for v2
new_row_loc={'Name':'V2','age':20,'city':'CIty1'}
df.loc[len(df.index)]=new_row_loc """

""" #Adding new row to df for v3
new_row_loc2={'Name':'V3','age':20,'city':'CIty2'}
df.loc[len(df.index)]=new_row_loc2 """

# ensures data directory present at root level
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

# define the file path
file_path=os.path.join(data_dir,'sample_data.csv')

# save the dataframe to csv file, including column names
df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path}")