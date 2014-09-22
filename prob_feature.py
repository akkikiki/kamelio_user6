#!/usr/bin/python
# coding:utf-8

"""
人気度の確率の素性を作る
python prob_feature.py prob.temp submission_data_v2.csv
"""
import sys
import csv

prob_dict = {}
for line in open(sys.argv[1]):
    itemList = line.strip().split()
    prob_dict[itemList[0]] = float(itemList[1])

flag = True
content_reader = csv.reader(open(sys.argv[2]))
for row in content_reader:
    if flag:
        print ",".join(row) + ",prob_feature"
        flag = False
        continue
    if row[1] in prob_dict:
        print ",".join(row) + ",",
        print prob_dict[row[1]]
    else:
        print ",".join(row),
        print "%f" %(0.0)
