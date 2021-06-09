# 读取数据库配置文件
config = {}
with open('app.config','r') as file:
    datas = file.readlines()
    for i in datas:
        if i.startswith('#'):
            continue
        key = i.split('=')[0]
        value = i.split('=')[1].replace('\n', '') # 字符串内置方法split()将字符串分隔开
        config[key] = value  # 填充字典的方法
if __name__ == '__main__':
    print(config)


