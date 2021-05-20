#### 前言

在测试用例中，执行完测试用例后，最后一步是判断测试结果是pass还是fail，自动化测试脚本里面一般把这种生成测试结果的方法称为断言（assert）。

用unittest组件测试用例的时候，断言的方法还是很多的，下面介绍几种常用的断言方法：assertEqual、assertIn、assertTrue

#### 基本断言方法

基本的断言方法提供了测试结果是True还是False。所有的断言方法都有一个msg参数，如果指定msg参数的值，则将该信息作为失败的错误信息返回。

序号	断言方法	断言描述
1	assertEqual(arg1, arg2, msg=None)	验证arg1=arg2，不等则fail
2	assertNotEqual(arg1, arg2, msg=None)	验证arg1 != arg2, 相等则fail
3	assertTrue(expr, msg=None)	验证expr是true，如果为false，则fail
4	assertFalse(expr,msg=None)	验证expr是false，如果为true，则fail
5	assertIs(arg1, arg2, msg=None)	验证arg1、arg2是同一个对象，不是则fail
6	assertIsNot(arg1, arg2, msg=None)	验证arg1、arg2不是同一个对象，是则fail
7	assertIsNone(expr, msg=None)	验证expr是None，不是则fail
8	assertIsNotNone(expr, msg=None)	验证expr不是None，是则fail
9	assertIn(arg1, arg2, msg=None)	验证arg1是arg2的子串，不是则fail
10	assertNotIn(arg1, arg2, msg=None)	验证arg1不是arg2的子串，是则fail
11	assertIsInstance(obj, cls, msg=None)	验证obj是cls的实例，不是则fail
12	assertNotIsInstance(obj, cls, msg=None)	验证obj不是cls的实例，是则fail

#### 一、简单案例

1.下面写了4个case，其中第四个是执行失败的

# coding:utf-8
import unittest
class Test(unittest.TestCase):
    def test01(self):
        '''判断 a == b '''
        a = 1
        b = 1
        self.assertEqual(a, b)

    def test02(self):
        '''判断 a in b '''
        a = "hello"
        b = "hello world!"
        self.assertIn(a, b)
    
    def test03(self):
        '''判断 a is True '''
        a = True
        self.assertTrue(a)
    
    def test04(self):
        '''失败案例'''
        a = "上海-悠悠"
        b = "yoyo"
        self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main()

2.执行结果如下

Failure
Expected :'\xe4\xb8\x8a\xe6\xb5\xb7-\xe6\x82\xa0\xe6\x82\xa0'
Actual   :'yoyo'
 <Click to see difference>

Traceback (most recent call last):
  File "D:\test\yoyotest\kecheng\test12.py", line 27, in test04
    self.assertEqual(a, b)
AssertionError: '\xe4\xb8\x8a\xe6\xb5\xb7-\xe6\x82\xa0\xe6\x82\xa0' != 'yoyo'
3.执行的结果，中文编码不对，没正常显示中文，遇到这种情况，可以自定义异常输出

二、自定义异常

1.以assertEqual为例分析：

assertEqual(self, first, second, msg=None)
    Fail if the two objects are unequal as determined by the '=='
    operator.

2.翻译：如果两个对象不能相等，就返回失败，相当于return: first==second

3.这里除了相比较的两个参数first和second，还有第三个参数msg=None,这个msg参数就是遇到异常后自定义输出信息



 

#### 三、unittest常用的断言方法

1.assertEqual(self, first, second, msg=None)

--判断两个参数相等：first == second

2.assertNotEqual(self, first, second, msg=None)

--判断两个参数不相等：first ！= second

3.assertIn(self, member, container, msg=None)

--判断是字符串是否包含：member in container

4.assertNotIn(self, member, container, msg=None)

--判断是字符串是否不包含：member not in container

5.assertTrue(self, expr, msg=None)

--判断是否为真：expr is True

6.assertFalse(self, expr, msg=None)

--判断是否为假：expr is False

7.assertIsNone(self, obj, msg=None)

--判断是否为None：obj is None

8.assertIsNotNone(self, obj, msg=None)
--判断是否不为None：obj is not None

————————————————
版权声明：本文为CSDN博主「**星空**」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_39247153/article/details/81082313



#### 有点像if条件分支的近亲

关键字 assert，当这个关键字后边的条件为假的时候，程序自动崩溃并抛出AssertionError的异常

>>> assert 3>4
>>> Traceback (most recent call last):
>>> File "<stdin>", line 1, in <module>
>>> AssertionError
>>> assert 3 < 4
>
>assert这个关键字我们称之为“断言”，当这个关键字后边的条件为假的时候，程序自动崩溃并抛出AssertionError的异常。
>什么情况下我们会需要这样的代码呢？当我们在测试程序的时候就很好用，因为与其让错误的条件导致程序今后莫名其妙地崩溃，不如在错误条件出现的那一瞬间我们实现“自爆”。
>一般来说我们可以用Ta再程序中置入检查点，当需要确保程序中的某个条件一定为真才能让程序正常工作的话，assert关键字就非常有用了。

逻辑上等同于


if not condition:
    raise AssertionError()

————————————————
版权声明：本文为CSDN博主「daduryi」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/daduryi/article/details/71123827