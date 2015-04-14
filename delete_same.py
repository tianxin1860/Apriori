#!/usr/bin/env python
# coding=utf-8


import sys


inputFile = sys.argv[1]
outputFile = sys.argv[2]

def PickDiff(inputFile, outputFile):
    with open(inputFile, 'r') as input:
        total = input.readlines()
        fact = set(total)
    with open(outputFile, 'w') as output:
        for line in fact:
            output.write(line)

PickDiff(inputFile, outputFile)
