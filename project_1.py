import numpy as np
import pandas as pd
pd.set_option("display.max_columns",None)

df = pd.read_excel(r"C:\Users\WIN\Downloads\Big_mart.xlsx",engine="openpyxl")
# print(df.head())
# df.info()


# print(df.isnull().sum())

df['Item_Identifier'].unique().sum()
# print(df['Item_Identifier'])


duplicate_count = df.duplicated(subset='Item_Identifier').sum()
# print(duplicate_count)


df['Item_Weight'].fillna(df['Item_Weight'].median(),inplace=True)

df['Outlet_Size'].fillna("NA",inplace=True)

# print(df[['Item_Weight','Outlet_Size']])


df['Item_Visibility'].replace(0,df['Item_Visibility'].median(),inplace=True)
df['Item_Visibility'] = round(df['Item_Visibility'],2)
df['Item_Visibility'] = np.where(df['Item_Visibility']< 0.05,'Low','High')
# print(df['Item_Visibility'])


df['Item_Outlet_Sales'] = round(df['Item_Outlet_Sales'],2)


df['Item_MRP'] = round(df['Item_MRP'],2)
# print(df['Item_MRP'])

df['Item_Fat_Content'] = df['Item_Fat_Content'].replace({'LF':'Low Fat','reg':'Regular',
                                                          'Regularural':'Regular'})


df.to_csv('Cleaned_Big_mart.csv')
print('File Saved Successfully')