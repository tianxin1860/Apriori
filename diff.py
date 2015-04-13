#!/usr/bin/env python
# coding=utf-8

'''To test how much lines if same beteween 2 files'''

import sys


trainFile = sys.argv[1]
testFile = sys.argv[2]


def BuildList(trainFile):
    with open(trainFile, 'r') as inputFile:
        list = inputFile.readlines() 
        return list



def compute(testFile):
    same = 0
    total = 0
    trainList = BuildList(trainFile)
    with open(testFile, 'r') as testFile:
        line = testFile.readline()
        while line:
            total += 1
            if line in trainList:
                same += 1
                line = testFile.readline()
            else:
                line = testFile.readline()
    print "same:%d    trainNumber:%d    testNumber:%d" %(same, len(trainList), total) 
    return same, len(trainList), total

compute(testFile)


