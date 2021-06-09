import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

dataset = pd.read_csv(r'E:\资料\IBM历史数据20000905-20200721.csv', index_col='日期', parse_dates=(['日期']))
# 数据整理
x = dataset.iloc[500:1000, 1:2].values
y = dataset.iloc[:500, 1:2].values


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
    ax.set_ylim(80, 230)
    ax.set_xlim(0, 500)
    ax.plot(test_result, color='r', label='IBM True Stock Price')
    ax.plot(predict_result, color='b', label='IBM Predicted Stock Price')
    plt.legend()
    plt.show()


dataset['高'][:500].plot(figsize=[15,7], legend=True)
dataset['高'][500:1000].plot(figsize=[15,7], legend=True)
plt.title('IBM Stock Price')
plt.show()
