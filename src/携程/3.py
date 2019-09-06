#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************
'''
def LevenshteinDis(str1, str2):
    m = len(str1)
    n = len(str2)

    distances = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        distances[i][0] = i
    for i in range(n+1):
        distances[0][i] = i
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                distances[i][j] = min(distances[i - 1][j - 1], min(distances[i - 1][j], distances[i][j - 1])) + 1
    return distances[m][n]

'''
def LevenshteinDis(str1, str2):
    longs = str1 if len(str1)>len(str2) else str2
    shorts = str2 if len(str1)>len(str2) else str1
    distance = [i for i in range(len(shorts)+1)]
    for i in range(1,len(longs)+1):
        pre=distance[0]
        distance[0]=i
        for j in range(1,len(shorts)+1):
            tmp=distance[j]
            if(longs[i-1]==shorts[j-1]):
                distance[j]=pre
            else:
                distance[j]=pre+1
            distance[j]=min(distance[j],distance[j-1]+1,tmp+1)
            pre=tmp
    return distance[len(shorts)]
# ******************************结束写代码******************************
try:
    _str1 = input()
except:
    _str1 = None

try:
    _str2 = input()
except:
    _str2 = None

res = LevenshteinDis(_str1, _str2)

print(str(res) + "\n")