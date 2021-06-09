import pandas as pd
import numpy as np
import matplotlib as plt
import os
import re
from sklearn.preprocessing import MinMaxScaler
from keras .models import Sequential
from keras.layers import Dense,LSTM,Dropout,GRU

s=0
dataset = pd.DataFrame()
data2 = pd.DataFrame()
path = list()
data= list()
x1 = list()
datefile = os.walk(r'D:\资料\Dataset\PHM 2010\PHM 2010\c1\c1')
for dirs,folders,fname in datefile:
    for name in fname:
        path.append(os.path.join(dirs,name))
for i in path:
    s+=1
    data1 = pd.read_csv(i)
    x = re.match(r'.*(c_\d_\d{3}).csv$',i).group(1)
    for d in range(5001):
        data2.append(data1.iloc[d*20])
    data.append(data2)
    x1.append(x)
    print(s)
