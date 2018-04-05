# -*- coding: utf-8 -*-
"""
bayes
"""
from math import log
import numpy as np

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

def createVocablist(dataset):
    vocabSet = set([])
    for document in dataset:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def word2vec(vocablist,inputset):
    returnvec = [0]*len(vocablist)
    for word in inputset:
        if word in inputset:
            if word in vocablist:
                returnvec[vocablist.index(word)] = 1
            else:
                print 'missing!'
    return returnvec

def trainNB(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = np.ones(numWords); p1Num = np.ones(numWords)
    p0Denom = 0.0; p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = map(lambda x:log(x/p1Denom),p1Num)          #change to log()
    p0Vect = map(lambda x:log(x/p0Denom),p0Num)          #change to log()
    return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify,p0Vec,p1Vec,pClass):
    p1 = sum(vec2Classify*p1Vec) + log(pClass)
    p2 = sum(vec2Classify*p0Vec) + log(1.0 - pClass)
    if p1 > p2:
        return 1
    else:
        return 0
    
if __name__ == '__main__':
    listOPosts,listClasses = loadDataSet()
    myVocablist = createVocablist(listOPosts)
    trainMat = []
    for postDoc in listOPosts:
        trainMat.append(word2vec(myVocablist,postDoc))
    print trainMat
    print '-----'
    print listClasses
    print '-----'
    p0V,p1V,pAb = trainNB(np.array(trainMat),np.array(listClasses))
    testEntry = ['love','my','dalmation']
    thisDoc = np.array(word2vec(myVocablist,testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
    testEntry = ['dog', 'dalmation']
    thisDoc = np.array(word2vec(myVocablist, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
