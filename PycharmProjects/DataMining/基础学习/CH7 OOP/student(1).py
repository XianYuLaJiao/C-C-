# 子类继承父类的特征（参数）和行为（方法）

from 基础学习.ch6.Person import Person


class Student(Person):  # 声明从父类Person继承，
    def __init__(self, name, height, stuo, school):  # 子类的构造函数如果要用到父类的特征参数
        # 也要写入构造函数中，并且可以添加子类自己的特征
        super().__init__(name, height)  # 继承父类的特征时，要用super（）函数调取父类的构造函数
        self.stuo = stuo
        self.school = school

    def do_homework(self):
        print('我叫' + self.name + ',我的学号是:' + self.stuo + ',我在' + self.school + '学校上学，我在写作业')


student1 = Student('焦健', 175, '1510141315', '湖北工业大学')
student1.do_homework()
student1.say()
student1.run()
