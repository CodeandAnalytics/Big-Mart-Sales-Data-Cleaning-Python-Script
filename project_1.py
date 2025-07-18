import numpy as np
import pandas as pd
pd.set_option("display.max_columns",None)

df = pd.read_excel(r"C:\Users\WIN\Downloads\Big_mart (1).xlsx",engine="openpyxl")
print(df.head())
print(df.tail())
df.info()


print(df.isnull().sum())


duplicate_count = df.duplicated(subset='Item_Identifier').sum()
print(duplicate_count)


df['Item_Weight'].fillna(df['Item_Weight'].median(),inplace=True)
df['Item_Weight'] = round(df['Item_Weight'],2)


df['Outlet_Size'].fillna("NA",inplace=True)
df['Outlet_Size'] = df['Outlet_Size'].replace("High","Large")
print(df[['Item_Weight','Outlet_Size']])


df['Item_Visibility'].replace(0,df['Item_Visibility'].median(),inplace=True)
df['Item_Visibility'] = round(df['Item_Visibility'],2)
df['Item_Visibility'] = np.where(df['Item_Visibility']< 0.05,'Low','High')
print(df['Item_Visibility'])


df['Item_Outlet_Sales'] = round(df['Item_Outlet_Sales'],2)
print(df['Item_Outlet_Sales'])


df['Item_MRP'] = round(df['Item_MRP'],2)
print(df['Item_MRP'])

df['Item_Fat_Content'] = df['Item_Fat_Content'].replace({'LF':'Low Fat','reg':'Regular',
                                                          'Regularural':'Regular'})
print(df['Item_Fat_Content'])

df.to_csv('Updated Big_mart.csv',index=False)
print('File Saved!')


