# -*- coding: utf-8 -*-
"""
knn
"""
import numpy as np
import operator
import matplotlib.pyplot as plt

def createDateset():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse=True)
    return sortedClassCount [0][0]

def file2matrix(filename):
    f = open(filename)
    arrayolines = f.readlines()
    numberoflines = len(arrayolines)
    returnMat = np.zeros((numberoflines,3))
    classLabelVector = []
    f = open(filename)
    index = 0
    for line in f.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataset):
    minVals = dataset.min(0)
    maxVals = dataset.max(0)
    ranges = maxVals - minVals
    normDataset = np.zeros(np.shape(dataset))
    m = dataset.shape[0]
    normDataset = dataset - np.tile(minVals,(m,1))
    normDataset = normDataset / np.tile(ranges,(m,1))
    return normDataset,ranges,minVals

def main(f,k):
    horatio = 0.10
    datingDataMat,datingLabels = file2matrix(file)
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*horatio)
    errorcount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],k)
        #print "the classifier came back with: %d, the real answer is: %d" %(classifierResult,datingLabels[i])
        if (classifierResult != datingLabels[i]):
            errorcount += 1.0
    #print "the total error rate is: %f" %(errorcount/float(numTestVecs))
    return (errorcount/float(numTestVecs))
if __name__ == '__main__':    
    '''
    group,labels = createDateset()
    for i in range(4):
        plt.scatter(group[i][0],group[i][1],linewidth=2.5)
    
    plt.xlim(xmax=2)
    plt.ylim(ymax=2)
    plt.show()
    '''
    file = "./datingTestSet2.txt"
    group,labels = file2matrix(file)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(group[:,1],group[:,2],15.0*np.array(labels),15.0*np.array(labels))
    plt.show()
    a = []
    b = []
    for i in range(1,800):
        er = main(file,i)
        a.append(i)
        b.append(er)
    plt.ylabel('error')
    plt.xlabel('time(s)')
    plt.plot(a,b,'r',label='error rate')
    plt.legend(bbox_to_anchor=[0.3, 1])
    plt.grid() 
    plt.show()
    print min(b),b.index(min(b))
    
