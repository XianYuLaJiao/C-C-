import re
import pandas as pd

# dataF = pd.DataFrame(columns=['X轴坐标', 'X轴偏差', 'Y轴坐标', 'Y轴偏差', 'Z轴坐标', 'Z轴偏差'])
# datum = s = dataset = 0
# list1 = []
# datadict = {}
# none = [None, None, None, None, None, None]
path = ['16L024267_20200929065832.dmo', '16L024268_20200929081351.dmo', '16L024269_20200929081742.dmo',
        '16L024269_20200929081742.dmo', '16L024271_20200929082254.dmo', '16L024272_20200929083051.dmo']
t = 0
# 读取数据 with open('16L024267_20200929065832.dmo', 'r', encoding='utf-8') as file1,
# open('16L024267_20200929065832.dmo', 'r', encoding='utf-8') as file2, open('16L024267_20200929065832.dmo', 'r',
# encoding='utf-8') as file2, open('16L024267_20200929065832.dmo', 'r', encoding='utf-8') as file4,
# open('16L024267_20200929065832.dmo', 'r', encoding='utf-8') as file5,open('16L024267_20200929065832.dmo', 'r',
# encoding='utf-8') as file6:
for p in path:
    t += 1
    dataF = pd.DataFrame(columns=['X轴坐标', 'X轴偏差', 'Y轴坐标', 'Y轴偏差', 'Z轴坐标', 'Z轴偏差'])
    datum = s = dataset = 0
    list1 = []
    datadict = {}
    none = [None, None, None, None, None, None]
    with open(p, 'r', encoding='utf-8') as file:
        data = file.readlines()


    #  根据UTPUT/ FA[(](.*)[)]提取焊点编号，切分列表数据
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
    # 去除第一个空数据
    data1 = list1[1:]

    # 正则表达式提取数据并且匹配焊点编号，写入字典中，
    for d in data1:
        car = re.match(r'OUTPUT/\sFA[(](\w*)[)].*TA[(](.*)[)]', d[0])
        if car.group(1) in datadict.keys():
            key1 = car.group(1)
            if car.group(2).endswith('X'):
                datadict[key1][0] = re.findall(r'-?\d+\.\d{3}', d[1])[0]
                datadict[key1][1] = re.findall(r'-?\d+\.\d{3}', d[3])[0]
            elif car.group(2).endswith('Y'):
                datadict[key1][2] = re.findall(r'-?\d+\.\d{3}', d[1])[1]
                datadict[key1][3] = re.findall(r'-?\d+\.\d{3}', d[3])[0]
            elif car.group(2).endswith('Z'):
                datadict[key1][4] = re.findall(r'-?\d+\.\d{3}', d[1])[2]
                datadict[key1][5] = re.findall(r'-?\d+\.\d{3}', d[3])[0]

        elif car.group(1) not in datadict.keys():
            key2 = car.group(1)
            if car.group(2).endswith('X'):
                none[0] = re.findall(r'-?\d+\.\d{3}', d[1])[0]
                none[1] = re.findall(r'-?\d+\.\d{3}', d[3])[0]
            elif car.group(2).endswith('Y'):
                none[2] = re.findall(r'-?\d+\.\d{3}', d[1])[1]
                none[3] = re.findall(r'-?\d+\.\d{3}', d[3])[0]
            elif car.group(2).endswith('Z'):
                none[4] = re.findall(r'-?\d+\.\d{3}', d[1])[2]
                none[5] = re.findall(r'-?\d+\.\d{3}', d[3])[0]
            datadict[key2] = none
            none = [None, None, None, None, None, None]

    # 字典转化为DataFrame形式
    datafinally = pd.DataFrame.from_dict(datadict, orient='index',
                                         columns=['X轴坐标', 'X轴偏差', 'Y轴坐标', 'Y轴偏差', 'Z轴坐标', 'Z轴偏差'])
    # dataF = pd.concat([dataF, datafinally], axis=1)
    datafinally.index.name = '焊点编号'
    datafinally.columns.name = '数据名称'
    print(datafinally)
    # datafinally.to_excel(r'C:\Users\jiaojian\Desktop\dataF'+str(t)+'.xlsx')
