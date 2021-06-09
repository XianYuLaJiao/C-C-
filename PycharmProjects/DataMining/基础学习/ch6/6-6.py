
def print_userinfo(name, gender='男', age=25, depart='FBI'):  # 在定义函数时，有多个参数，形式参数要在前，默认值参数在后面
    print('我是'+name)
    print('我是'+gender+'生')
    print('我今年'+str(age)+'岁')
    print('我在'+depart+'工作')


print_userinfo('小明', '男', '22', '美国国家情报局')
print('--'*30)#分割线
print_userinfo('小明')
print('--'*30)#分割线
print_userinfo('小明', age=30,depart='IAA',)  # 关键字参数可以覆盖默认值参数，并且关键字参数，不需要对应顺序，
# 和默认值参数一样，要排在必要参数后面#必要参数要在关键字参数前边，因为首先调用的是必要参数，其次是关键字参数，其中关键字参数的前后顺序无所谓。
print('--'*30)#分割线

