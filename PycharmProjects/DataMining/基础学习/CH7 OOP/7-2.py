"""


"""


# 什么是函数？什么是方法？
# 函数是在面向过程中的称呼，在面向对像中，类里面定义的函数称为方法。

class Person:
    """类的说明"""
    height = 180

    def __init__(self, height):  # 调用python内置方法,__init__也叫构造函数，是python内置的所以左右
        # 两边双下划线,__init__()构造函数是在实例化过程中自动被调用一次。
        print('i am a person objecct')
        self.height = height  # 实例属性（实例变量参数），self代表实例对象本身，它和后面的属性不同
        # 它起的是代表作用，不可更改，也不是参数，后面的变量即形式参数，是表示属性的参数，在实例调用时就是
        # 参数的意思


# 自定义方法，和内置的构造函数的区别有一点，内置方法不用return，自定义方法需要return返回值
    def say(self):  # 方法的定义参数要有self，相当于无参的函数.在调用方法时不需要有参数。
        print('i am speaking')
        return 'haha'


person = Person()
person.say()  # 调用不需要写self
print(person.say())
