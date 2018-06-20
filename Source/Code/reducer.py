#!/usr/bin/env python

import sys
import ast
import operator

def Add_Data():
    list1 = []
    list2 = []
    for line in sys.stdin:
        key, value = line.strip().split('\t')
        list = ast.literal_eval(key)
        if (list[0] == 'A'):
            list1.append([list[1], list[2], int(value)])
        elif (list[0] == 'B'):
            list2.append([list[1], list[2], int(value)])
    Mul_Data(list1,list2)

def Mul_Data(list1,list2):
    dict = {}
    key_Val_list = []
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if (list1[i][1] == list2[j][0]):
                val = list1[i][2] * list2[j][2]
                key1 = "{0},{1}".format(list1[i][0], list2[j][1])
                key_Val_list.append([key1, val])

    for i in range(0,len(key_Val_list)):
        if(key_Val_list[i][0] in dict.keys()):
            dict[key_Val_list[i][0]] += key_Val_list[i][1]

        else:
            dict[key_Val_list[i][0]] = key_Val_list[i][1]

    Print_Data(dict)


def Print_Data(dict):
    for k, v in sorted(dict.items()):
        print(k, v)

if __name__ == '__main__':
    Add_Data()