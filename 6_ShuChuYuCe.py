import pandas as pd
import numpy as np
import sys
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
import json
import joblib

class Result:
    precision = 0
    recall = 0
    accuracy = 0
    rocX = []
    rocY = []
    featureImportances = []

params = {}
params['model'] = r'E:/EXweek3/GBDTmodel.model'
params['test'] = r'E:/EXweek3/verify_tiqu.csv'
params['opath'] = r'E:/EXweek3/result1.csv'
argvs = sys.argv

try:
    for i in range(len(argvs)):
        if i < 1:
            continue
        if argvs[i].split('=')[1] == 'None':
            params[argvs[i].split('=')[0]] = None
        else:
            Type = type(params[argvs[i].split('=')[0]])
            params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])

    model = joblib.load(params['model'])    
    test_csv = pd.read_csv(params['test'])
    test_feature = test_csv.drop(['label'], axis=1)
    y_pred = model.predict_proba(test_feature)
    y_pred = model.predict(test_feature)
    
    predict_df = pd.DataFrame(y_pred)
    predict_df.columns = ['predict']
    predict_df.to_csv(params['opath'],index = False)

    
    res = {}
    res['fMeasure'] = f1_score(test_csv['label'], y_pred , average='macro')   
    res['precision'] = precision_score(test_csv['label'], y_pred , average='macro')   
    res['recall'] = recall_score(test_csv['label'], y_pred , average='macro')   
    res['accuracy'] = accuracy_score(test_csv['label'], y_pred)   
    
    print(json.dumps(res))
except Exception as e:
    print(e)
    #============================ 模型测试及输出 ==================================

data_test = r'C:\Users\shuimu666\Desktop\dataset\test_tiqu.csv'
data_test = np.array(pd.read_csv(data_test))
data_test0 = data_test

from sklearn.impute import SimpleImputer

imp = SimpleImputer(missing_values=np.nan, strategy='mean')
data_test1 = data_test[:, :-1]
data_test = imp.fit_transform(data_test1)
filename = data_test0[:,14] 
predictions = model.predict(data_test)

output = pd.DataFrame({'label':predictions,'filename':filename})
output.to_csv(r'C:\Users\shuimu666\Desktop\dataset\resulttest.csv',index = False)
output.head()

