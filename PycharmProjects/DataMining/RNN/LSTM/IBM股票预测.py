import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

dataset = pd.read_csv(r'E:\资料\IBM历史数据19801124-20000905.CSV', index_col='date')


def plot_predictions(test_result, predict_result):
    """
    :param test_result: 真实值测试结果
    :param predict_result: 预测值结果
    :return:
    """
    fig = plt.figure(figsize=25 * 10, dpi=500)
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.set_xlable('time', fontsize='20')
    ax.set_ylable('stock price', fontsize='20')
    ax.set_ylim(70, 150)
    ax.set_xlim(0, 5005)
    ax.plot(test_result, color='r', label='IBM True Stock Price')
    ax.plot(predict_result, color='b', label='IBM Predicted Stock Price')


def date001(x):
    date002 = re.match(r'(\d{4})年(\d*)月(\d*)', str(x))
    nian = date002.group(1)
    yue = date002.group(2)
    ri = date002.group(3)
    date003 = nian + '-' + yue + '-' + ri
    return date003



da = pd.DataFrame(dataset.index)
print(da)
dataset.index = da['date'].apply(lambda x: date001(x))
print(dataset.head())
