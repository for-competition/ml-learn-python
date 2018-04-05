# -*- coding: utf-8 -*-
"""
decision tree plot
"""
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth",fc="0.8")
leafNode = dict(boxstyle="round4",fc="0.8")
arrow_aargs = dict(arrowstyle="<-")

def plotnode(nodetxt,centerpt,parentpt,nodetype):
    createPlot.ax1.annotate(nodetxt, xy=parentpt,xycoords='axes fraction', 
                            xytext=centerpt, textcoords='axes fraction',
                            va='center',ha='center',bbox=nodetype,arrowprops=arrow_aargs)

def createPlot():
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotnode('a decision node',(0.5,0.1),(0.1,0.5),decisionNode)
    plotnode('a leaf node',(0.8,0.1),(0.3,0.8),leafNode)
    plt.show()
    
def getleafnum(mytree):
    leafnum = 0
    firstStr = mytree.keys()[0]
    secondDict = mytree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            leafnum += getleafnum(secondDict[key])
        else:
            leafnum += 1
        return leafnum

def getTreedepth(mytree):
    maxDepth = 0
    firstStr = mytree.keys()[0]
    secondDict = mytree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == "dict":
            thisDepth = 1+getTreedepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
        return maxDepth
    
def retrieveTree(i):
    listoftrees = [{'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}},
                   {'no surfacing':{0:'no',1:{'flippers':{0:{'head':{0:'no',1:'yes'}},1:'no'}}}}
                   ]
    return listoftrees[i]

def plotmidtext(cntrpt,parentpt,txtstring):
    xmid = (parentpt[0]-cntrpt[0])/2.0 + cntrpt[0]
    ymid = (parentpt[1]-cntrpt[1])/2.0 + cntrpt[1]
    createPlot.ax1 = plt.subplot(111, frameon=False)
    createPlot.ax1.text(xmid,ymid,txtstring)

def plotree(mytree,parentpt,nodetxt):
    leafnum = getleafnum(mytree)
    firstStr = mytree.keys()[0]
    cntrpt = (plotree.xOff + (1.0 + float(leafnum))/2.0/plotree.totalw,plotree.yOff)
    plotmidtext(cntrpt,parentpt,nodetxt)
    plotnode(firstStr,cntrpt,parentpt,decisionNode)
    secondDict = mytree[firstStr]
    plotree.yOff = plotree.yOff - 1.0/plotree.totald
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotree(secondDict[key],cntrpt,str(key))
        else:
            plotree.xOff = plotree.xOff + 1.0/plotree.totalw
            plotnode(secondDict[key],(plotree.xOff,plotree.yOff),cntrpt,leafNode)
            plotmidtext((plotree.xOff,plotree.yOff),cntrpt,str(key))
    plotree.yOff = plotree.yOff + 1.0/plotree.totald

    
def createplotree(intree):
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks=[],yticks=[])
    createplotree.ax1 = plt.subplot(111,frameon=False,**axprops)
    plotree.totalw = float(getleafnum(intree))
    plotree.totald = float(getTreedepth(intree))
    plotree.xOff = -0.5/plotree.totalw;
    plotree.yOff = 1.0;
    plotree(intree,(0.5,1.0),'')
    plt.show()
    
        
        
