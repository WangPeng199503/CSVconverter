from tkinter import *
from tkinter.filedialog import askdirectory
import pandas as pd
from glob import glob
import os

def selectPath():
    path_ = askdirectory()
    path.set(path_)


def MultiCsvReader():
    #生成修改后文件存放文件夹，命名为ModifiedFile
    global path
    choose_path = path.get()
    newpath= choose_path+'\\'+'ModifiedFile'

    #判断ModifiedFile文件夹是否存在，不存在则新建
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    else:
        output_ = '请确认是否已存在ModifiedFile文件夹'

    #获取当前目录下所有csv格式文件
    os.chdir(choose_path)
    csv_list = glob('*.csv')

    #对文件夹中的csv文件批量进行处理
    for i in csv_list:

        #按顺序读取文件 i为文件名
        os.chdir(choose_path)
        df = pd.read_csv(i)
        WindTurbineNumbr = df.iat[0,0]#获取风机号
        #跳过前三行并删除最后一行
        df = pd.read_csv(i ,header = 3, sep = ';',dtype = 'str')
        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)#删除最后一列

        #生成csv文件 将风机号写入文件名中
        os.chdir(newpath)
        num = WindTurbineNumbr.split(':')
        i = num[1] + '#_' + i
        df.to_csv(i, index = False)    

    
    output_ = 'Conventer OK'
    output.set(output_)
    
root = Tk()
path = StringVar()
output = StringVar()

Label(root,text = "目标文件夹:").grid(row = 0, column = 0)
Entry(root, textvariable = path).grid(row = 0, column = 1)
Button(root, text = "文件夹选择", command = selectPath).grid(row = 0, column = 2)

Label(root,text = "转换结果:").grid(row = 1, column = 0)
Entry(root, textvariable = output).grid(row = 1 , column = 1)
Button(root, text = "文件转换", command = MultiCsvReader).grid(row = 1 , column =2)

root.mainloop()