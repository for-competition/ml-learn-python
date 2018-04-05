#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import main

def id3(dataset):
    numFeatures = len(dataset[0]) - 1
    baseEntropy = main.entropy(dataset,0)
    bestInfogain = 0.0; bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataset]
        uniquevals = set(featList)
        newEntropy = 0.0
        for value in uniquevals:
            subDataset = main.splitDataset(dataset,i,value)
            prob = len(subDataset)/float(len(dataset))
            newEntropy += prob*main.entropy(subDataset,0)
        infogain = baseEntropy - newEntropy
        if(infogain > bestInfogain):
            bestInfogain = infogain
            bestFeature = i
    return bestFeature

def c4_5(dataset):
    numFeatures = len(dataset[0]) - 1
    baseEntropy = main.entropy(dataset,0)
    bestGainratio = 0.0; bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataset]
        uniquevals = set(featList)
        newEntropy = 0.0
        for value in uniquevals:
            subDataset = main.splitDataset(dataset,i,value)
            prob = len(subDataset)/float(len(dataset))
            newEntropy += prob*main.entropy(subDataset,0)
        infogain = baseEntropy - newEntropy
        splitinfo = main.entropy(dataset,i)
        Gainratio = infogain/splitinfo
        if(Gainratio > bestGainratio):
            bestGainratio = Gainratio
            bestFeature = i
    return bestFeature

                    