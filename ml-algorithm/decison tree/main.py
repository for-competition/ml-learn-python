# -*- coding: utf-8 -*-
"""
decision tree
"""
from math import log
import operator
import pickle
import alg
import plot_decision_tree as treeplotter

def createDataset():
    dataset = [[1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataset,labels

def entropy(dataset,i):
    numEntries = len(dataset)
    labelcounts = {}
    for featvec in dataset:
        currnentLabel = featvec[i-1]
        if currnentLabel not in labelcounts.keys():
            labelcounts[currnentLabel] = 0
        labelcounts[currnentLabel] +=1
    ent = 0.0
    for key in labelcounts:
        prob = float(labelcounts[key])/numEntries
        ent -= prob*log(prob,2)
    return ent

def splitDataset(dataset,axis,value):
    retDateset =[]
    for featvec in dataset:
        if featvec[axis] == value:
            reducedFeatvec = featvec[:axis]
            reducedFeatvec.extend(featvec[axis+1:])
            retDateset.append(reducedFeatvec)
    return retDateset
    
def majoritycnt(classlist):
    classcount = {}
    for vote in classlist:
        if vote not in classcount.keys():
            classcount[vote] = 0
        classcount[vote] += 1
    sortedClasscount = sorted(classcount.items(),key = operator.itemgetter(1),reverse =True)
    return sortedClasscount[0][0]

def createtree(dataset,labels,func):
    classlist = [example[-1] for example in dataset]
    if classlist.count(classlist[0]) == len(classlist):
        return classlist[0]
    if len(dataset[0]) == 1:
        return majoritycnt(classlist)
    bestfeat = func(dataset)
    bestfeatlabel = labels[bestfeat]
    mytree = {bestfeatlabel:{}}
    del(labels[bestfeat])
    featvalues = [example[bestfeat] for example in dataset]
    uniquevals = set(featvalues)
    for value in uniquevals:
        sublabels = labels[:]
        mytree[bestfeatlabel][value] = createtree(splitDataset(dataset,bestfeat,value),sublabels,func)
    return mytree

def classify(inputree,featlabels,testvec):
    firstStr = inputree.keys()[0]
    secondDict = inputree[firstStr]
    featIndex = featlabels.index(firstStr)
    for key in secondDict.keys():
        if testvec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classlabel = classify(secondDict[key],featlabels,testvec)
            else:
                classlabel = secondDict[key]
    return classlabel

def storetree(inputree,filename):
    fw = open(filename,'w')
    pickle.dump(inputree,fw)
    fw.close()
    
def grabtree(filename):
    fr = open(filename)
    return pickle.load(fr)

if __name__ == '__main__':
    file = './lenses.txt'
    f = open(file)
    lenses = [inst.strip().split('\t') for inst in f.readlines()]
    lensesLabels = ['age','prescript','astigmatic','tearRate']
    lensesTree = createtree(lenses,lensesLabels,alg.c4_5)
    lensesTree
    treeplotter.createplotree(lensesTree)
                             