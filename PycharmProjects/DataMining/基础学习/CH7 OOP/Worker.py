# 工人继承人类
from 基础学习.ch6.Person import Person


class Worker(Person):
    def __init__(self, name, height, factory ):
        super().__init__(name, height)
        self.factory = factory


    def work(self):
        print()
