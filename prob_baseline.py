#!/usr/bin/python
#coding:utf-8

import sys

prob_dict = {}
for line in open(sys.argv[1]):
    itemList = line.strip().split()
    prob_dict[itemList[0]] = float(itemList[1])

#
submission_file = open(sys.argv[2])
submission_file.readline()
for line in submission_file:
    itemList = line.strip().split(',')
    if itemList[1] in prob_dict:
        if prob_dict[itemList[1]] <= 0.1:
            print line.strip() + "," + '"NULL"'
        else:
            print line.strip() + "," + '"article_read"'
		
