import pandas as pd
import os
import sys

# 合并文件
params = {}
params['Folder_Path'] = 'E:/EXweek3/data'                                   # 文件夹路径
params['SaveFile_Path'] = 'E:/EXweek3/test.csv'                     # 合并文件路径
argvs = sys.argv
try:
    # 引入文件列表
    os.chdir(params['Folder_Path'])
    file_list = os.listdir()
    # 表头引入
    df = pd.read_csv(params['Folder_Path'] +'\\'+ file_list[0])
    df2 = df[['DE_time','FE_time']][0: 3000]
    df2 = df[['DE_time','FE_time']][0: 3000].copy()
    df2['label'] = 'TEST01.csv'
    df2.to_csv(params['SaveFile_Path'], encoding="utf_8_sig",index=False)
    # 从表头顺延
    for i in range(1,len(file_list)):
        df = pd.read_csv(params['Folder_Path'] + '\\'+ file_list[i])
        df2 = df[['DE_time','FE_time']][0: 3000]
        df2 = df[['DE_time','FE_time']][0: 3000].copy()
        df2['label'] = str('TEST'+str(i+1)+'.csv')
        df2.to_csv(params['SaveFile_Path'],encoding="utf_8_sig",index=False, header=False, mode='a+')

except Exception as e:
    print(e)