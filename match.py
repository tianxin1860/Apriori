#!/usr/bin/env python
# coding=utf-8

#using sequence a*b to match the blank word


_DEBUG = False
#_DEBUG = True

from collections import defaultdict
import sys
import random

DICT = defaultdict(int)

def BuildDict(list):
    '''(key,value), key = (action1, action2, action3), value = number'''
    length = len(list)
    index = 1
    while index < length-1:
        key = (list[index-1], list[index], list[index+1])
        DICT[key] += 1
        index+=1


def mysort(ResultList):
    list = sorted(ResultList, key = lambda x:x[1], reverse = True)
    return list


def FindPossible(context):
    '''return list, element is a tuple ,the key contains str, value is the times of concurrence'''
    ResultList = []
    for key in DICT.keys():
        context_dict = (key[0], key[2])
        if cmp(context_dict, context) == 0:
            tuple = (key[1], DICT[key])
            ResultList.append(tuple)
    list = sorted(ResultList, key = lambda x:x[1], reverse = True)
    return list

with open(sys.argv[1], 'r') as InputFile:
    line = InputFile.readline()
    while line:
        line = line.strip().split(' ')
        BuildDict(line)
        line = InputFile.readline()


def ComputeAccuracy():
    total_blank = 0
    right_count = [0] * 20
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
                print
            while i < blank_count:
                context = (line[index_list[i]-1], line[index_list[i]+1])
                result = FindPossible(context)
                correct_word = line[index_list[i]]
                if _DEBUG == True:
                    print "blank %d:%s" %(i, correct_word)
                    print "result:%d" % len(result)    
                    print result
                for set_size in range(1, 21):  
                    for word in result[0:set_size]:
                        if word[0] == correct_word:
                            right_count[set_size-1] += 1
                i += 1
                if _DEBUG == True:
                    print
            if _DEBUG == True:
                print "\n"    
            line = TestFile.readline()    
    set_size = 0        
    for right in right_count:
        set_size += 1
        accuracy =float(right)/total_blank        
        print "test number:%d   set_size:%-2d    total_blank:%d    right_count:%-2d    accuracy:%f"  %(sentence_count, set_size, total_blank, right, accuracy)


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
