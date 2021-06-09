import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense,LSTM,Dropout
from keras.optimizers import SGD# 随机梯度下降法

dataset = pd.read_csv(r'E:\资料\IBM历史数据19801124-20000905.csv', index_col='date', parse_dates=(['date']))


def date001(x):
    date002 = re.match(r'(\d{4}).?(\d*).?(\d*)',x)
    nian = date002.group(1)
    yue = date002.group(2)
    ri =date002.group(3)
    date003 = nian + '-' + yue + '-' +ri
    return date003
da = pd.DataFrame(dataset.index)
dataset.index = da['date'].apply(lambda x: date001(x))
print(dataset.head())

#检查数据是否有缺失值
train_set = dataset[:'1986-10-10':-1].iloc[:,0:1]
test_set = dataset['1986-10-10':'1988-10-10':-1].iloc[:,0:1]


def plot_predictions(test_result, predict_result):
    """
    :param test_result: 真实值测试结果
    :param predict_result: 预测值结果
    :return:
    """
    fig = plt.figure(figsize=[15, 7], dpi=120)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlabel('time', fontsize='10')
    ax.set_ylabel('stock price', fontsize='10')
    ax.plot(test_result, color='r', label='IBM True Stock Price')
    ax.plot(predict_result, color='b', label='IBM Predicted Stock Price')
    plt.legend()
    plt.show()

dataset['开盘'][:'1986-10-10':-1].plot(figsize=[25,8], legend=True,color='b')
dataset['开盘']['1986-10-10':'1988-10-10':-1].plot(figsize=[25,8], legend=True,color='g')
plt.title('IBM Stock Price')
plt.legend(["1990","1980"])
plt.show()

# 归一化：将每一维的特征映射到指定区间：【0，1】
sc = MinMaxScaler(feature_range=[0,1])# 最大最小值归一化
train_set_scaled = sc.fit_transform(train_set)
train_set_scaled

# 创建序列数据集（训练和测试）
# 60个时间步为一个样本，1输出
x_train = []
y_train = []
for i in range(60, 1487):
    x_train.append(train_set_scaled[i - 60:i, 0])
    y_train.append(train_set_scaled[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)


# LSTM输入:(samples, sequence_length, features)
# 将训练集重构，转换成LSTM网络可以识别的数据reshape:训练集(2700,60) --->(2700 , 60 , 1)
x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

model = Sequential()
#LSTM 第一层
model.add(LSTM(128,return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))

# 第二层
model.add(LSTM(128, return_sequences=True))
model.add(Dropout(0.2))

#第三层
model.add(LSTM(128))
model.add(Dropout(0.2))

# Dense层
model.add(Dense(units=1))

# 模型编译
model.compile(optimizer='rmsprop',loss='mse')

# 训练模型
model.fit(x_train, y_train, epochs=40, batch_size=60)

dataset_total = pd.concat((dataset['开盘'][:'1986-10-10':-1],dataset['开盘']['1986-10-10':'1988-10-10':-1]),axis=0)
# 获取输入数据
inputs = dataset_total[len(dataset_total)-len(test_set) - 60:].values
# 归一化
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)

# 准备测试集进行预测
x_test = []
for i in range(60, 566):
    x_test.append(inputs[i - 60:i, 0])

x_test = np.array(x_test)

x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

predict_test = model.predict(x_test) # 预测
predict_stock_price = sc.inverse_transform(predict_test)
plot_predictions(test_set, predict_stock_price)
