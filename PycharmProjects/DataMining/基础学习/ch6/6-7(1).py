
# 可变参数 一个*表示是一个序列元组类型的可变参数 可以理解为*value代表着无限多的空位，代表这个函数可以接受多个参数，
# 两颗星**是代表字典类型的可变参数
# def test(*value):
#     print(type(value))
#     for v in value:#(*value是序列类型,在value传进来之后直接被封装成一个元组，即*value是把value变成元组，所以可以遍历它)
#        print(v)
#
#
#
# test('hellow world')
# print('---'*9)
# test('1234', 'hellow', 'big bang', 'dsdsdsd')#括号内输入的是四个字符串，所以是四个参数
# print('---'*9)
# test(['1234', 'hellow', 'big bang', 'dsdsdsd'])#括号内输入的是一个序列，所以是一个参数
# print('---'*9)
# test(('1234', 'hellow', 'big bang', 'dsdsdsd'))#括号内输入的是一个元组，所以是一个参数

# 结果：
# <class 'tuple'>
# hellow world
# ---------------------------
# <class 'tuple'>
# 1234
# hellow
# big bang-
# dsdsdsd
# ---------------------------
# <class 'tuple'>
# ['1234', 'hellow', 'big bang', 'dsdsdsd']
# ---------------------------
# <class 'tuple'>
# ('1234', 'hellow', 'big bang', 'dsdsdsd')


