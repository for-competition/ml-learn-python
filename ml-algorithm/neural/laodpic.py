#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from PIL import Image
from pylab import *
import numpy as np

def fun(x,x1,x2):
    return -0.00001*(x-x1)*(x-x2)


dog = array(Image.open("/Users/didi/Downloads/dog.jpg"))
shuai = array(Image.open("/Users/didi/Downloads/shuai.jpeg"))
shuai1 = shuai[1:500]

for i in range(0,334):
    for j in range(0,500):
        for k in range(0,3):
            a = fun(i,-100,434)
            b = fun(i,-100,600)
            shuai1[i][220+j][k] = shuai1[i][220+j][k] + a*b*dog[i][j][k]

Image.fromarray(shuai1)




x = np.arange(142,157,0.1) 
#设定 y 轴，载入刚才的正态分布函数
y = normfun(x, mean, std)
plt.plot(x,y)
#画出直方图，最后的“normed”参数，是赋范的意思，数学概念
plt.hist(time, bins=10, rwidth=0.9, normed=True)
plt.title('Time distribution')
plt.xlabel('Time')
plt.ylabel('Probability')
#输出
plt.show()
