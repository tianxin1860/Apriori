#!/usr/bin/env python
# coding=utf-8


import sys

input = sys.argv[1]

def seperate(input):
    with open(input, 'r') as fp:
        inputFile = fp.readlines()
        length = len(inputFile)
        if length > 5000:
            inputFile = inputFile[:5000]
        else:
            print "the length is too short"
    train =  open('train.txt', 'w')
    test =  open('test.txt', 'w')
    for i in range(5000):
        if (i+1) % 10 == 0:
            test.write(inputFile[i])
        else:
            train.write(inputFile[i])
    train.close()
    test.close()

seperate(input)
