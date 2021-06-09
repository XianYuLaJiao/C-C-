class Person:
    Name = '蔡徐坤'
    Height = 180

    def __init__(self, name, height):
        self.Name = name
        self.Height = height
        print('我是对象：' + self.Name)

    def say(self):
        print('我的身高为：' + str(self.Height))


# person1 = Person()
person2 = Person('焦健', 175)  # 实例化传入两个参数，直接调到构造函数中。
person2.say()  # 调用say（）方法

