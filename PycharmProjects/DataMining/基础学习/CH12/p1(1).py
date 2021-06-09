__all__ = ['a', 'Kid', 'Add']  #模块主动控制访问调取权限，只有__alla__内的可以被外界调用
a, b = 1, 7


def Add(x, y):
    return x + y


class Kid:
    def __init__(self, age):
        self.age = age

    def laugh(self):
        print('我今年%d岁了' % self.age)



















