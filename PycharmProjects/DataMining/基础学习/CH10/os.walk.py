

import os # 目标遍历当前工作文件夹内所有的文件和路径，并且进行分类表示 通过序列解包
for dirpath,subdir,files in os.walk(os.getcwd()):
    for name in subdir:
        print('目录',os.path.join(dirpath,name))
    for name in files:
        print('----'*9,'文件',os.path.join(dirpath,name))

# -------------
# --------------- ('D:\\PycharmProjects\\Anaconda3\\001\\基础学习\\CH10', ['newfile-os', '__pycache__'], ['10-1.py', '10-3.py', '10-4.py', '10-5.py', '10-6.py', 'app.config', 'appConfig.py', 'data.txt', 'dataw.txt', 'datazwen', 'datazwen1.txt', 'os.walk.py'])
# --------------- ('D:\\PycharmProjects\\Anaconda3\\001\\基础学习\\CH10\\newfile-os', [], [])
# --------------- ('D:\\PycharmProjects\\Anaconda3\\001\\基础学习\\CH10\\__pycache__', [], ['appConfig.cpython-38.pyc'])
