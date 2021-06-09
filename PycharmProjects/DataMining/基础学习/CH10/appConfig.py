
config = {}
with open('app.config','r') as file:
    datas = file.readlines()
    for i in datas:
        if i.startswith('#'):
            continue
        key = i.split('=')[0]
        value = i.split('=')[1].replace('\n','')
        config[key] = value
if __name__ == '__main__':
    print(config)
