
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import sklearn as sk


# In[3]:

data=pd.read_csv('F:/regression.csv',sep=',',encoding='gbk')
data.head(5)


# In[36]:

data.dtypes


# In[4]:

data[list(range(1,6))]


# In[10]:

from sklearn import preprocessing
imp = sk.preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(data[list(range(1,6))])


# In[4]:

data1=data.iloc[:,1:6]
data1


# In[5]:

x = data1.iloc[:,1:5] 
y = data1.iloc[:,0]


# In[66]:

X_train,X_test, y_train, y_test = sk.cross_validation.train_test_split(x,y,test_size=0.2, random_state=1)


# In[69]:

print X_train.shape  
print y_train.shape  
print X_test.shape  
print y_test.shape 


# In[7]:

from sklearn import linear_model
linreg = linear_model.LinearRegression()


# In[92]:

model=linreg.fit(X_train, y_train)  
print model  
print linreg.intercept_  
print linreg.coef_ 


# In[79]:

y_pred = linreg.predict(X_test)  
print y_pred  


# In[81]:

print type(y_pred),type(y_test)  
print len(y_pred),len(y_test)  
print y_pred.shape,y_test.shape 


# In[83]:

#均方根误差(Root Mean Squared Error, RMSE)
sum_mean=0  
for i in range(len(y_pred)):  
    sum_mean+=(y_pred[i]-y_test.values[i])**2  
sum_erro=np.sqrt(sum_mean/37)  
# calculate RMSE by hand  
print "RMSE by hand:",sum_erro


# In[93]:

plt.figure()  
plt.plot(range(len(y_pred)),y_pred,'b',label="predict")  
plt.plot(range(len(y_pred)),y_test,'r',label="test")  
plt.legend(loc="upper right") #显示图中的标签 
plt.ylabel('number of real orders')  
plt.show()


# In[94]:

error = []
for i in range(len(y_pred)):  
    error.append(y_pred[i]-y_test.values[i])  


# In[95]:

error


# In[8]:

#交叉验证
rmse=[]
conf=[]
enter=[]
for i in range(1000):
    X_train,X_test, y_train, y_test = sk.cross_validation.train_test_split(x,y,test_size=0.2)
    model=linreg.fit(X_train, y_train)
    y_pred = linreg.predict(X_test)
    sum_mean=0  
    for i in range(len(y_pred)):  
        sum_mean+=(y_pred[i]-y_test.values[i])**2  
    sum_erro=np.sqrt(sum_mean/37)
    rmse.append(sum_erro)
    conf.append(linreg.coef_ )
    enter.append(linreg.intercept_)


# In[9]:

min(rmse)


# In[10]:

rm=sorted(rmse)
rm[0:500]


# In[35]:

rmse.index(1239.3898034779738)


# In[36]:

rmse[840]


# In[37]:

conf[840]


# In[38]:

enter[840]


# BEST in LinearRegression:Y = 0.64776848 X1+ 1.3947606 X2 +  0.1700415 X3 -0.58988382 X4

# In[16]:

#树回归

from sklearn.tree import DecisionTreeRegressor
treereg = DecisionTreeRegressor(max_depth=10000)
rmse=[]
for i in range(10):
    X_train,X_test, y_train, y_test = sk.cross_validation.train_test_split(x,y,test_size=0.2)
    model=treereg.fit(X_train, y_train)
    y_pred = treereg.predict(X_test)
    sum_mean=0  
    for i in range(len(y_pred)):  
        sum_mean+=(y_pred[i]-y_test.values[i])**2  
    sum_erro=np.sqrt(sum_mean/37)
    rmse.append(sum_erro)


# In[17]:

rmse


# In[45]:

rs={}
for d in range(4,16):
    treereg = DecisionTreeRegressor(max_depth=d)
    rmse=[]
    for i in range(10):
        X_train,X_test, y_train, y_test = sk.cross_validation.train_test_split(x,y,test_size=0.2)
        model=treereg.fit(X_train, y_train)
        y_pred = treereg.predict(X_test)
        sum_mean=0  
        for i in range(len(y_pred)):  
            sum_mean+=(y_pred[i]-y_test.values[i])**2  
        sum_erro=np.sqrt(sum_mean/37)
        rmse.append(sum_erro)
    rs.setdefault(d,[]).append(rmse)


# In[46]:

rs


# In[31]:

from sklearn.ensemble import RandomForestRegressor
rdreg = RandomForestRegressor(max_depth=5,bootstrap=True,n_estimators = 500)
rmse=[]
for i in range(10):
    X_train,X_test, y_train, y_test = sk.cross_validation.train_test_split(x,y,test_size=0.2)
    model=rdreg.fit(X_train, y_train)
    y_pred = rdreg.predict(X_test)
    sum_mean=0  
    for i in range(len(y_pred)):  
        sum_mean+=(y_pred[i]-y_test.values[i])**2  
    sum_erro=np.sqrt(sum_mean/37)
    rmse.append(sum_erro)


# In[32]:

rmse


# In[36]:

from sklearn.ensemble import GradientBoostingRegressor
gdbtreg = GradientBoostingRegressor(max_depth=5,n_estimators = 100)
rmse=[]
for i in range(10):
    X_train,X_test, y_train, y_test = sk.cross_validation.train_test_split(x,y,test_size=0.2)
    model=rdreg.fit(X_train, y_train)
    y_pred = rdreg.predict(X_test)
    sum_mean=0  
    for i in range(len(y_pred)):  
        sum_mean+=(y_pred[i]-y_test.values[i])**2  
    sum_erro=np.sqrt(sum_mean/37)
    rmse.append(sum_erro)


# In[37]:

rmse


# In[ ]:



