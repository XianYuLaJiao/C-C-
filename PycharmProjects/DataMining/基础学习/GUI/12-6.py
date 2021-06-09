# 模拟登录
from tkinter import *


def zc():
    def zc1():

        if str(passwordnew.get()) is str(passwordnew1.get()):
            print(yhmnew.get())
            print(passwordnew.get())
            with open('db_password', 'a', encoding='utf-8') as file:
                file.write('bd_' + str(yhmnew.get()) + '=' + str(passwordnew.get()))
            varnhsa2.set('注册成功')
        else:
            varnhsa2.set('密码不一致，请重新输入')

    root1 = Tk()
    root1.title('7201注册系统')
    root1.geometry('400x300+350+180')

    passwordnew = StringVar()
    passwordnew1 = StringVar()
    yhmnew = StringVar()

    topframenew = Frame(root1)

    inputLabelnew = Label(topframenew, text='用户名:', fg='black', font='宋体 20')
    inputLabelnew.pack(side=LEFT, padx=5, pady=5)

    inputEntrynew = Entry(topframenew, textvariable=yhmnew)
    inputEntrynew.pack(side=LEFT, padx=5, pady=5)

    topframenew.pack(pady=10)

    sframenew = Frame(root1)

    pwLabelnew = Label(sframenew, text='密码:', fg='black', font='宋体 20')
    pwLabelnew.pack(side=LEFT, padx=5, pady=5)

    pwEntrynew = Entry(sframenew, textvariable=passwordnew)
    pwEntrynew.pack(side=LEFT, padx=5, pady=5)

    sframenew.pack()

    sframenew1 = Frame(root1)

    pwLabelnew1 = Label(sframenew1, text='确认密码:', fg='black', font='宋体 20')
    pwLabelnew1.pack(side=LEFT, padx=5, pady=5)

    pwEntrynew1 = Entry(sframenew1, textvariable=passwordnew1)
    pwEntrynew1.pack(side=LEFT, padx=5, pady=5)

    sframenew1.pack()

    pwButtonnew1 = Button(root1, text='注册', fg='orange', command=zc1)
    pwButtonnew1.pack()

    varnhsa2 = StringVar()
    varnhsa2.set('k')

    jieguoLabel1 = Label(root1, fg='orange', textvariable=varnhsa2, font='微软雅黑 30')
    jieguoLabel1.pack()

    print(varnhsa2.get())

    ppf = Label(root1, fg='orange', text=varnhsa2, font='微软雅黑 30')
    ppf.pack()

    root1.mainloop()


def chark():
    db_ = {}
    db = {}
    with open('db_password', 'r', encoding='utf-8') as file:
        registerdata = file.readlines()
        yhm1 = yhm.get()
        password1 = password.get()
        db['db_' + str(yhm1)] = str(password1)
        for i in registerdata:
            key = i.split('=')[0]
            value = i.split('=')[1].replace('\n', '')
            db_[key] = value
        else:
            y = set(db_.items())
            p = set(db.items())
            if p.issubset(y):
                varnhsa.set('%s你好骚啊！！！！' % yhm1)
            else:
                varnhsa.set('有内鬼，中止交易，over！')


root = Tk()
root.title('7201登录系统')
root.geometry('600x400+250+150')

password = StringVar()
yhm = StringVar()

topframe = Frame(root)

inputLabel = Label(topframe, text='用户名:', fg='black', font='宋体 20')
inputLabel.pack(side=LEFT, padx=5, pady=5)

inputEntry = Entry(topframe, textvariable=yhm)
inputEntry.pack(side=LEFT, padx=5, pady=5)

inputButton = Button(topframe, text='登录', fg='blue', command=chark)
inputButton.pack(side=LEFT)

topframe.pack(pady=10)

sframe = Frame(root)

pwLabel = Label(sframe, text='密码:', fg='black', font='宋体 20')
pwLabel.pack(side=LEFT, padx=5, pady=5)

pwEntry = Entry(sframe, textvariable=password)
pwEntry.pack(side=LEFT, padx=5, pady=5)

pwButton = Button(sframe, text='注册', fg='orange', command=zc)
pwButton.pack(side=LEFT)

sframe.pack()

varnhsa = StringVar()
varnhsa.set('请输入用户名和密码')

jieguoLabel = Label(root, fg='green', textvariable=varnhsa, font='微软雅黑 30')
jieguoLabel.pack()

root.mainloop()
