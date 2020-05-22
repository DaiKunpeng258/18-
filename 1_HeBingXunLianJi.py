import pandas as pd
import os

# 合并文件
params = {}
params['Folder_Path'] = 'E:/EXweek3/train'           # 文件夹路径
params['SaveFile_Path'] = 'E:/EXweek3'                        # 合并文件路径
params['TrainFileName'] = 'train.csv'                         # 合并训练集文件名
params['TestFileName'] = 'verify.csv'                         # 合并测试集文件名

try:
    # 引入文件列表
    os.chdir(params['Folder_Path'])
    file_list = os.listdir()
    # 训练集表头引入
    df = pd.read_csv(params['Folder_Path'] +'\\'+ file_list[0])
    df2 = df[['DE_time','FE_time']]
    df2 = df[['DE_time','FE_time']].copy()
    df2['label'] = 1
    df2.to_csv(params['SaveFile_Path']+'\\'+ params['TrainFileName'],encoding="utf_8_sig",index=False)
    # 测试集表头引入
    df = pd.read_csv(params['Folder_Path'] +'\\'+ file_list[4])
    df2 = df[['DE_time','FE_time']]
    df2 = df[['DE_time','FE_time']].copy()
    df2['label'] = 1
    df2.to_csv(params['SaveFile_Path']+'\\'+ params['TestFileName'],encoding="utf_8_sig",index=False)
    # 从表头顺延
    for i in range(1,len(file_list)):
        df = pd.read_csv(params['Folder_Path'] + '\\'+ file_list[i])
        df2 = df[['DE_time','FE_time']]
        df2 = df[['DE_time','FE_time']].copy()
        # 添加标签
        if 'B' == file_list[i][0]:
            df2['label'] = 1
        elif 'I' == file_list[i][0]:
            df2['label'] = 3
        elif 'N' == file_list[i][0]:
            df2['label'] = 0
        else:
            df2['label'] = 2
        # 按顺序划分
        if i % 4 != 0:
            df2.to_csv(params['SaveFile_Path']+'\\'+ params['TrainFileName'],encoding="utf_8_sig",index=False, header=False, mode='a+')
        elif i == 4:
            continue
        else:
            df2.to_csv(params['SaveFile_Path']+'\\'+ params['TestFileName'],encoding="utf_8_sig",index=False, header=False, mode='a+')

except Exception as e:
    print(e)