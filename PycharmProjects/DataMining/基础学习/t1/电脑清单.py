sum1 = 0
complist = {'Cpu': 3000, 'Gpu': 1500, '显示器': 1500, '主板': 850, '内存': 700, '硬盘': 1000, '电源': 500, }
# list1 = list(complist.values())
# for i in list1:
#     sum1 = sum1 + i
# print('电脑一共:', str(sum1), sep='')
list2 = list(complist.keys())
for key in list2:
    print(key + ':', complist[key])
    sum1 = sum1 + complist[key]
else:
    print('一共:', sum1)

