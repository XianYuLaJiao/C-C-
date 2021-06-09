# 读取的过程 1.打开文件 2.读取文件 3.关闭文件
# r : read只读
# w : write只写
# a+ :读写

file = open('data.txt', 'r')  # 第一步 打开文件，其中‘data.txt’表示是省略了目录，默认是和10-1同目录
# print(file.readable()) # 判断是否可读
# data = file.read(6)  # 按字符读取，无参着是全读，有参则读相应个字符

# data = file.readline()  # 按行一行一行读取
# while data:
#     print(data, end='')
#     data = file.readline()
# file.close()

# datas = file.readlines()  # 按多行读取
# print(type(datas))
# for line in datas:
#     print(line, end='')
# file.close()

# 相对路径 绝对路径
# file1 = open('d:\\学习资料\\DATA.txt', 'r')  # 这里是绝对路径
# data1 = file1.readlines()
# print(data1)
# for line in data1:
#     print(line, end='')
# file1.close()
# file.close()

# with语句，
with open('d:/学习资料/DATA.txt','r') as file: # 用with语句可以将open 和 close 之间的语句块化，
    # 执行，就不需要最后特地关闭文件了
    data2 = file.readlines()
    print(data2)



