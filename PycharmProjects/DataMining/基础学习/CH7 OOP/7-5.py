class Person:
    Name = '蔡徐坤'
    Height = 180

    def __init__(self, Name, Height):
        self.name = Name
        self.__height = Height  # 属性左前加两个下划线，表示类内部的私有变量，只能类内部访问
        self.height = Height
        print('我是对象：' + self.name)

    def say(self):  # 实例方法
        print('我的身高为：' + str(self.height))

    # def __say(self):  #和私有变量一样 ，前边健双下划线表示私有方法，被保护起来，不能被外部调用

    def getHeight(self):
        # 定义一个访问私有变量的方法，检查权限，通过才可以调用
        # 检查访问所有变量__Height__的资格
        return self.__height

    def setHeight(self, height):
        # 定义一个修改私有变量的方法，检查权限，通过才可以修改
        self.__height = height

    @classmethod  # 类方法,修饰器
    def classcount(cls):
        print('我是类方法' + cls.Name)


person1 = Person('王宝强', 164)
person1.classcount()
person1.say()
Person.classcount()  # 无参的，直接用类方法访问，不用实例化直接调用类方法，用类名直接调用

# person1 = Person()
# person2 = Person('焦健', 175)
# person2.say()  # 调用say（）方法

person3 = Person('私有变量', 200)
b = person3.getHeight
print(str(b))
person3.setHeight(201)
c = person3.getHeight
print(str(c))
