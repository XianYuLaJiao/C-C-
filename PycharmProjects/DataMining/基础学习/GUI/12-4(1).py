from tkinter import *


def tax_calc():
    inputCount = inputVar.get()
    print(inputCount)


root = Tk()
root.title('月输入计算器')
root.geometry('400x400+350+200')


inputLable = Label(root, text='请输入月收入：', bg='pink', font='微软雅黑 20', )
inputLable.pack(padx=10,pady=10)

inputVar = StringVar()


inputEntry = Entry(root, textvariable=inputVar) # 单行文本输入快
inputEntry.pack(pady=10)


inputButton = Button(root, text='计算', command=tax_calc)
inputButton.pack(pady=10)

outputVar = StringVar()
outputVar.set('点击计算')
outputLable = Label(root, textvariable=outputVar, fg='green', font ='微软雅黑 28' )
outputLable.pack(padx=5,pady = 8)


root.mainloop()