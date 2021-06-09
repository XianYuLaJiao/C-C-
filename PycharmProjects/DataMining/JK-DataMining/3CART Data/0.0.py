import re
import pandas as pd

dataF = pd.DataFrame(columns=['X轴坐标', 'X轴偏差', 'Y轴坐标', 'Y轴偏差', 'Z轴坐标', 'Z轴偏差'])
datum = s = dataset = 0
list1 = []
datadict = {}
none = [None, None, None, None, None, None]
path = ['16L024267_20200929065832.dmo', '16L024268_20200929081351.dmo', '16L024269_20200929081742.dmo',
        '16L024269_20200929081742.dmo', '16L024271_20200929082254.dmo', '16L024272_20200929083051.dmo']
# 读取数据 with open('16L024267_20200929065832.dmo', 'r', encoding='utf-8') as file1,
# open('16L024267_20200929065832.dmo', 'r', encoding='utf-8') as file2, open('16L024267_20200929065832.dmo', 'r',
# encoding='utf-8') as file2, open('16L024267_20200929065832.dmo', 'r', encoding='utf-8') as file4,
# open('16L024267_20200929065832.dmo', 'r', encoding='utf-8') as file5,open('16L024267_20200929065832.dmo', 'r',
# encoding='utf-8') as file6:
# for p in path:
with open('16L024268_20200929081351.dmo', 'r', encoding='utf-8') as file:
    data = file.readlines()


# 根据UTPUT/ FA[(](.*)[)]提取焊点编号，切分列表数据
def lis(ele):
    element = re.match(r'OUTPUT/\sFA[(](\w*)[)]', ele)
    if element:
        name = element.group(1)
    return element


for i in data:
    datum += 1
    if lis(i):
        list0 = data[dataset - 1:datum - 1]
        list1.append(list0)
        s += 1
        dataset = datum
print(list1)
# 去除第一个空数据
data1 = list1[1:]
print(data1)
