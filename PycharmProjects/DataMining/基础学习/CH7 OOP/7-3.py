class Person:  # 定义一个类，打个比方，定义一种动物
    """类的说明"""
    height = 180  # 类属性，是被所有实例共享的，不归任何实例所有，不会被实例改变的

    # 类属性是基础属性，所有实例对象可以共享，当然具体实例对象可以自己在基础类属性上有特征，
    # 其在类属性范畴内

    def __init__(self):  # 方法相当于为类添加行为动作，
        print('i am a person objecct')

    @property
    def say(self):
        print('i am speaking')
        return 'haha'


person = Person() # 实例化即定义具体的对象，创造一个对象叫person，并且归于Person类的范畴，
# 它两之间是子类和父类的关系，就像具体的对象是大象，大象归于动物这一个大类里面一样，并且动物会动，
# 动就是行为动作，能干什么，这就是类的方法，则实例化的对象大象也会动。另外动物都有鼻子，鼻子就是
# 类属性，则实例化对象大象也有鼻子，但是每一个具体实例化的对象属性不一样，这就叫对象的特征，人的
# 鼻子短，大象的鼻子长，但都是动物都有鼻子
# person.say()
# print(person.say())
person = Person()
person1 = Person()
print(person.height)  #实例属性没有自行定义的话，默认调用类属性。
print(person1.height)
print(Person.height)
print(person.__dict__)
print(person1.__dict__)
print(Person.__dict__)