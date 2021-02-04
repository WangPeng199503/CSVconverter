import pandas as pd
from glob import glob

#读取CSV文件
df = pd.read_csv('Datalog_2021_01_06_20_38_28.csv')
WindTurbineNumbr = df.iat[0,0]#获取风机号
SECversion = df.iat[1,0]#获取版本号

df = pd.read_csv('Datalog_2021_01_06_20_38_28.csv',header = 3, sep = ';',dtype = 'str')#跳过前三行读取
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)#删除最后一列

df.to_csv('combined_column.csv', index = False)#所有数据保存



'''
#删除第二行 和 第三行
df = df.drop(df.index[0:2])
df = df.reset_index(drop = True)'''

#删除前三行
df = df.drop(df.index[0:3])
df = df.reset_index(drop = True)
print(df)

#将变量名行作为列索引后 删除变量名行
column = list(df.iloc[0])
df.columns = column
print(column)
print(df)
#df = df.drop(df.index[0:1]) 
'''
#将Timestamp作为行索引后 删除Timestamp列
index = list(df.Timestamp)
df.index = index
df = df.drop(['Timestamp'], axis = 1) 


#生成csv文件
df.to_csv('combined_column.csv', index = False, header = False)'''