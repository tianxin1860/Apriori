#!/usr/bin/env python
# coding=utf-8

_DEBUG = False

from collections import defaultdict
import sys
import random

DICT = defaultdict(int)

def BuildDict(list):
    length = len(list)
    index = 0
    while index < length-1:
        key = list[index] + ' ' + list[index+1]
        DICT[key] += 1
        index+=1


def mysort(ResultList):
    list = sorted(ResultList, key = lambda x:x[1], reverse = True)
    return list


def FindPossible(str):
    ResultList = []
    for key in DICT.keys():
        set = frozenset(key.split(' '))
        if str in set:
            tuple = (key, DICT[key])
            ResultList.append(tuple)
    return mysort(ResultList)

with open(sys.argv[1], 'r') as InputFile:
    line = InputFile.readline()
    while line:
        line = line.strip().split(' ')
        BuildDict(line)
        line = InputFile.readline()


def ComputeAccuracy():
    total_blank = 0
    right_count = 0
    sentence_count = 0
    with open(sys.argv[2], 'r') as TestFile:
        line = TestFile.readline()
        while line:
            sentence_count += 1
            line = line.strip().split(' ')
            length = len(line)
            value = [1] * length
            tuple_list = zip(line, value)
            sentence = map(list, tuple_list)
            blank_count = int(length * 0.1)
            index_list = GenerateRandom(blank_count, length)
            total_blank += blank_count
            for index in index_list:
                sentence[index][1] = 0
            i = 0
            if _DEBUG == True:
                print "sentence %d:" %sentence_count
                print sentence
            while i < blank_count:
                result = []
                list_result = FindPossible(line[index_list[i]-1])
                correct_word = line[index_list[i]]
                if _DEBUG == True:
                    print "blank %d:%s" %(i, correct_word)
                    print list_result
                for word_pair in list_result:
                    candidate =  word_pair[0].split(' ')
                    candidate.remove(line[index_list[i]-1])
                    item_result = (candidate[0], word_pair[1])
                    result.append(item_result)
                if _DEBUG == True:
                    print "result:"    
                    print result
                for word in result:
                    if word[0] == correct_word:
                        right_count += 1
                i += 1
            if _DEBUG == True:
                print "\n"    
            line = TestFile.readline()    
    accuracy =float(right_count)/total_blank        
    print "test number:%d   total_blank:%d    right_count:%d    accuracy:%f" %(sentence_count, total_blank, right_count, accuracy)



def GenerateRandom(count, length):
    i = 0
    flag_list = [0] * length
    index_list = []
    while (i < count):
        random_index = random.randint(1,length-2)
        if(flag_list[random_index] == 0 and flag_list[random_index-1] == 0 and flag_list[random_index+1] == 0):
            index_list.append(random_index)
            flag_list[random_index] = 1
            i += 1
        else:
            continue
    return index_list
    

ComputeAccuracy()
