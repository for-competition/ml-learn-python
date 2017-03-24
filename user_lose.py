
# coding: utf-8

# In[19]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.preprocessing import Imputer
from sklearn.cross_validation import train_test_split 
from sklearn.linear_model import LogisticRegression


# In[7]:

import sklearn
help(sklearn)


# In[11]:

data=pd.read_csv('F:/data.csv')


# In[12]:

data.head(5)


# In[20]:

imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(data)


# In[41]:

data.fillna(0)


# In[27]:

def plot_pr(auc_score, precision, recall, label=None):  
    pylab.figure(num=None, figsize=(6, 5))  
    pylab.xlim([0.0, 1.0])  
    pylab.ylim([0.0, 1.0])  
    pylab.xlabel('Recall')  
    pylab.ylabel('Precision')  
    pylab.title('P/R (AUC=%0.2f) / %s' % (auc_score, label))  
    pylab.fill_between(recall, precision, alpha=0.5)  
    pylab.grid(True, linestyle='-', color='0.75')  
    pylab.plot(recall, precision, lw=1)      
    pylab.show()


# In[39]:

x = data.iloc[:,1:37] 
y = data.iloc[:,40]


# In[36]:

x.head(5)


# In[42]:

y.head(5)


testNum = 10  
for i in range(0, testNum):  
     #加载数据集，切分数据集80%训练，20%测试  
     x_train, x_test, y_train, y_test\  
         = train_test_split(movie_data, movie_target, test_size = 0.2)  
		 
     #训练LR分类器  
clf = LogisticRegression()  
clf.fit(x_train, y_train)  
y_pred = clf.predict(x_test)  
p = np.mean(y_pred == y_test)  
print(p)  
average += p 
     
     #准确率与召回率  
answer = clf.predict_proba(x_test)[:,1]  
precision, recall, thresholds = precision_recall_curve(y_test, answer)      
report = answer > 0.5  
print(classification_report(y_test, report, target_names = ['neg', 'pos']))  
print("average precision:", average/testNum)  
print("time spent:", time.time() - start_time)  
   
plot_pr(0.5, precision, recall, "pos")

# In[ ]:



