with open('datazwen', 'w') as file:
    file.write('人生苦短，我用python')

with open('datazwen', 'r') as file:
    print(file.read())

# open（）的解码 encoding的默认为GBK编码方式
with open('datazwen1.txt', 'r', encoding='utf-8') as file:
    print('1-----------')
    print(file.read())

