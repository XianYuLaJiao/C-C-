# 自定义函数(若自定义的函数名和内置函数名相同了，则自定义函数覆盖内置函数，所以一般不要和内置函数相同，也可以采用大小写的差别区分开。)
# def funcname(params):
#     pass#语句块
# 1，定义一个打印‘hellowworld’字符串的方法
# # 2.定义一个打印指定字符串的方法
# # 3.定义一个计算加法的函数 a+b
# def Print():
#     print('hellowworld')
#
# Print()
# 结果：hellowworld
# def Print(s):#s代表参数
#     print(s)
# ms = 'hellow world'
# Print(ms)

# #结果:hellow world

# def Add(a, b):
#     # 不是所有的函数都有return，没有return相当于return了None，比如print函数没有返回值，也可以说返回值是空None
#     result = a + b
#     return result
#
#
# c = Add(1, 3)#将返回值赋予到变量c，接着用print打印出来
# print(c)
# 结果：4
def Add_Sub(a, b):
    sum = a + b
    sub = a - b
    return sum, sub
#
# # c = Add_Sub(4, 1)
# # print(c)
# # print(c[0],c[1])
# # print(type(c))
# # 结果；(5, 3)得到的是组元
# # 5 3
# # <class 'tuple'>
#
# sum, sub = Add_Sub(4, 1) #序列解包
# print(sum, sub)
# 结果：5 3




