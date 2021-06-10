import re
import pandas as pd

path = ['16L024267_20200929065832.dmo', '16L024268_20200929081351.dmo', '16L024269_20200929081742.dmo',
        '16L024269_20200929081742.dmo', '16L024271_20200929082254.dmo', '16L024272_20200929083051.dmo']
t = date1 = time1 = 0
writer = pd.ExcelWriter(r'C:\Users\17180\Desktop\3CART Data.xlsx')


def lis(ele):
    element = re.match(r'OUTPUT/\sFA[(](\w*)[)]', ele)
    if element:
        return element  # name = element.group(1)


def datetime(dt):
    global date1, time1
    date = re.match(r'DATE\s=\s(.{10})$', dt)
    time = re.match(r'TIME\s=\s(\d{2}:\d{2}:\d{2})$', dt)
    if date:
        date1 = date.group(1)
    if time:
        time1 = time.group(1)
    return [date1, time1]


for p in path:
    n = path[t][0:9]
    t += 1
    datum = s = dataset = 0
    list1, datetime1 = [], []
    datadict = {}
    none = [None, None, None, None, None, None, None, None, None, None, None]
    with open(p, 'r', encoding='utf-8') as file:
        data = file.readlines()
    for i in data:
        datetime1 = datetime(i)
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
                datadict[key1][2] = re.findall(r'\d{3},\s(\w{5}$)', d[3])[0]
            elif car.group(2).endswith('Y'):
                datadict[key1][3] = re.findall(r'-?\d+\.\d{3}', d[1])[1]
                datadict[key1][4] = re.findall(r'-?\d+\.\d{3}', d[3])[0]
                datadict[key1][5] = re.findall(r'\d{3},\s(\w{5}$)', d[3])[0]
            elif car.group(2).endswith('Z'):
                datadict[key1][6] = re.findall(r'-?\d+\.\d{3}', d[1])[2]
                datadict[key1][7] = re.findall(r'-?\d+\.\d{3}', d[3])[0]
                datadict[key1][8] = re.findall(r'\d{3},\s(\w{5}$)', d[3])[0]
            datadict[key1][9] = datetime1[0]
            datadict[key1][10] = datetime1[1]
        elif car.group(1) not in datadict.keys():
            key2 = car.group(1)
            if car.group(2).endswith('X'):
                none[0] = re.findall(r'-?\d+\.\d{3}', d[1])[0]
                none[1] = re.findall(r'-?\d+\.\d{3}', d[3])[0]
                none[2] = re.findall(r'\d{3},\s(\w{5}$)', d[3])[0]
            elif car.group(2).endswith('Y'):
                none[3] = re.findall(r'-?\d+\.\d{3}', d[1])[1]
                none[4] = re.findall(r'-?\d+\.\d{3}', d[3])[0]
                none[5] = re.findall(r'\d{3},\s(\w{5}$)', d[3])[0]
            elif car.group(2).endswith('Z'):
                none[6] = re.findall(r'-?\d+\.\d{3}', d[1])[2]
                none[7] = re.findall(r'-?\d+\.\d{3}', d[3])[0]
                none[8] = re.findall(r'\d{3},\s(\w{5}$)', d[3])[0]
            none[9] = datetime1[0]
            none[10] = datetime1[1]
            datadict[key2] = none
            none = [None, None, None, None, None, None, None, None, None, None, None]

    # 字典转化为DataFrame形式
    data_finally = pd.DataFrame.from_dict(datadict, orient='index',
                                          columns=['X轴坐标', 'X轴偏差', 'X-IN/OUT', 'Y轴坐标', 'Y轴偏差', 'Y-IN/OUT', 'Z轴坐标',
                                                   'Z轴偏差', 'Z-IN/OUT', '日期', '时间'])
    data_finally.index.name = '焊点编号'
    data_finally.columns.name = '数据名称'
    data_finally.to_excel(writer, sheet_name=n)
writer.save()
