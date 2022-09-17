#%%
#K-决策树
from math import log

def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-= prob * log(prob,2)
    return shannonEnt

#按照给定特征划分数据集
def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataset:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def createDataSet():
    dataSet=[[1,1,'yes'],
             [1,1,'yes'],
             [1,0,'no'],
             [0,1,'no'],
             [0,1,'no']]
    labels=['no surfacing','flippers']
    return dataSet,labels
#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    beseEntropy=calcShannonEnt(dataSet)
    bestInfoGain=0.0; bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet) / float(len(dataSet))
            newEntropy+=prob * calcShannonEnt(subDataSet)
        infoGain=beseEntropy-newEntropy
        if (infoGain>bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature

if __name__=='__main__':
    dataset,labels=createDataSet()
    bestFeature=chooseBestFeatureToSplit(dataset)
    #retDataSet=splitDataSet(dataset,1,1)
    #shannonEnt=calcShannonEnt(dataset)
    print(bestFeature)
    pass
# %%
