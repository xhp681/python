#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def cleardataset():
    filename='data/tnb-ysdata.xlsx'
    outfilename='data/tnb-newdata.csv'
    data=pd.read_excel(filename)
    data.dropna(inplace=True)   #删除Nan数据
    data.drop_duplicates()  #删除重复数据
    #data.drop(columns=['序列'],axis=1)
    #data.drop(columns=['序列'],axis=1)
    #data.to_csv(outfilename,encoding='utf-8')
    df=data[u'组方']
    print(df)

if __name__=='__main__':
    cleardataset()
    pass
# %%
