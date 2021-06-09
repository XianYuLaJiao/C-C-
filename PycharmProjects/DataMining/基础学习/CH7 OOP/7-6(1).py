class Person:
    Name = '焦健'
    Height = 175
    count = 0
    def __init__(self,Name , Height):
        self.name = Name
        self.height = Height
        Person.count +=1  # 这里类名可以用__class__替代，不需要记住具体的类名，
        # 与类方法内的cls差不多
        print('我是第' + str(Person.count) + '个实例'+'我叫' + self.name)

    def say(self):
        print('i am' + self.name)

    @classmethod
    def classcount(cls):
        print('一共实例化了'+ str(cls.count) + '个实例化对象')  #cls只能在类方法内使用，
        # 在__init__内不能有cls代表类


person1 = Person('cxk', 180)
person2 = Person('jiao', 190)
Person.classcount()

# 对象的三个特征 值Value 地址ID 类型Type,不同实例，即使特征一模一样，值一样，类型一样，但是
# 实例化的地址不一样，也就不是同一个实例，互不干扰
