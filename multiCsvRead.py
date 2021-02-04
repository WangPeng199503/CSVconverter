import pandas as pd
from glob import glob
import os

#获取桌面路径
path = os.path.join(os.path.expanduser("~"),'Desktop')

#生成修改后文件存放文件夹，命名为ModifiedFile
newpath= path+'\\'+'ModifiedFile'

#判断ModifiedFile文件夹是否存在，不存在则新建
if not os.path.exists(newpath):
    os.mkdir(newpath)

#获取当前目录下所有csv格式文件
csv_list = glob('*.csv')
csv_num = len(csv_list)

#对文件夹中的csv文件批量进行处理
for i in csv_list:
    #按顺序读取文件 i为文件名
    os.chdir(path)
    df = pd.read_csv(i, header = None)

    #删除第二行 和 第三行
    df = df.drop(df.index[1:3])
    df = df.reset_index(drop = True)

    #生成csv文件
    os.chdir(newpath)
    df.to_csv(i)
    










