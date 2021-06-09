# 将数据写入文件方式 1，打开文件 2，写文件 3，关闭文件
with open('dataw.txt','w') as file: # 这里如果是打开一共不存在的文件名，则直接新建一个文件
    # data = 'sdsdsdsd sdsdds fgfhjfmjjg djdkjf' # 文件写入必选是str数据
    # file.write(data+'\n')
    # data = 'wo s di er hang'
    # file.write(data)
    datas = ['hellow python','i am asniper','like'] #多行写入，可以用列表将字符串封装起来，
    # 写入功能没有自动换行的功能，需要自己添加'\n'方法有以下三种
    # for data in datas:  #第一种 用循环一个一个元素写入并且后边加换行符
    #     file.write(data+'\n')
    # file.writelines([data+'\n'for data in datas]) # 用列表推导式生成新的各元素后自带换行符
    # 的新列表，但这种方法会在最后多占一行空行，因为最后一个字符串后带有‘\n’即最后字符串写入后换行了
    file.write('\n'.join(datas))
    # write(str)是写入一共字符串，writelines(str,list)是写入多个字符串以列表的方式写入多个字符串，
    # 也可以写入一个字符串

    # 文件读取写入方式有
    # [r,w,a]  打开文本文件
    # [r+,w+,a+] 和第一种有细微的差别
    # [rb,wb,ab] 打开二进制的文件，图片，视频，声音
    # [rb+,wb+,ab+]
    # r读模式的四种读取文件，之前必选是文件已存在，只读的方式是必需是读已经存在的文件
    # w写入和a追加模式是可以直接open（）里面新建文件，或者写已存在文件。
