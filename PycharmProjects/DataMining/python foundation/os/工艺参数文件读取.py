import os
import re
t = 0

# def get_name_size():

root0 = r'C:\Users\jiaojian\Desktop\工艺参数'
for root, dirs, files in os.walk(root0):
    jgname = re.match(r'.*(\d\w{5}$)', root)
    if jgname:
        jb = jgname.group(1)
        for fname in files:
            re.match(r'.*bsl\d*r\d', fname)
        break
