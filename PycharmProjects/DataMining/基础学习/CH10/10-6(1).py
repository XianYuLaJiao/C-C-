# 目录OS

import os
import shutil

#
# print(os.path.exists('data.txt'))  #判断文件是否存在
#
# os.mkdir('newfile-os')  # 在当前目录下创建新的文件夹即目录，mkdir()方法只能在已经存在的文件夹下生成文件夹
# print(os.getcwd())  # D:\PycharmProjects\Anaconda3\001\基础学习\CH10
#
# os.rmdir('data.txt')   # 删除目录的方法,权限不大，只能删除空文件夹，防止删除有用文件
# shutil.rmtree('data.txt')  # 是删除目录，不管是不是空目录，可以删除非空目录，权限更加强大，谨慎使用

# 以上都是用的相对路径的方式，默认是在项目所在的目录里，直接生成写入文件名的文件夹
# 用绝对路径的方式也是可以的。在写入文件夹时写入路径和文件夹名称

# if os.path.exists('d:\\学习资料\\newfile_os'):
#     os.rmdir('d:\\学习资料\\newfile_os')
# else:
#     os.mkdir('d:\\学习资料\\newfile_os')
print('-------------')

for files in os.walk(os.getcwd()):  # os.walk返回的是一个迭代器，；里面是一个元组，
    print('---------------', files)

# 结果：是几个有三个元素的元组，元组第一个元素是代表路径的字符串，第二元素是表示前面目录下的目录文件夹的列表，第三元素是路径下的文件名的列表
# os.walk还有递归分类的功能，他打开路径下所有的文件夹和子文件夹，并且通过前面相同的方式显示出文件。
# C:\ProgramData\Anaconda3\python.exe D:/PycharmProjects/Anaconda3/001/基础学习/CH10/10-6.py
# -------------
# --------------- ('D:\\PycharmProjects\\Anaconda3\\001\\基础学习\\CH10', ['newfile-os', '__pycache__'], ['10-1.py', '10-3.py', '10-4.py', '10-5.py', '10-6.py', 'app.config', 'appConfig.py', 'data.txt', 'dataw.txt', 'datazwen', 'datazwen1.txt', 'os.walk.py'])
# --------------- ('D:\\PycharmProjects\\Anaconda3\\001\\基础学习\\CH10\\newfile-os', [], [])
# --------------- ('D:\\PycharmProjects\\Anaconda3\\001\\基础学习\\CH10\\__pycache__', [], ['appConfig.cpython-38.pyc'])

# 创建多级目录用os.makedirs(多级目录路径)，比os.mkdir()更加强大，可以生成多级文件目录，os.mkdir()只能生成一级

# 删除文件用，os.remove('datazwen'),删除文件
