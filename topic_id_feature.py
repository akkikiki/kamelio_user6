#!/usr/bin/python
#coding:utf-8
"""
topic_idの頻度を正規化した素性
python topic_id_feature.py training_data.csv training_data.csv > traning.topic_id_feature.csv
python topic_id_feature.py training_data.csv submission_data_v2.csv > submission.topic_id_feature.csv
"""

import sys
import csv
from collections import defaultdict
topic_id_dict = defaultdict(lambda:0)
content_reader = csv.reader(open(sys.argv[1]))

for row in content_reader:
    if row[3] == 'article_read':
        topic_id_dict[row[1]] += 1

max_freq = max(topic_id_dict.values())

feature_dict = {}
for key,value in topic_id_dict.items():
    feature_dict[key] = float(value)/max_freq

#for i,j in feature_dict.items():
#    print i,j

frag = True
content_reader = csv.reader(open(sys.argv[2]))
for row in content_reader:
    if frag:
        print ",".join(row)+",topic_id_feature"
        frag = False
        continue
    if row[1] in feature_dict:
        print ",".join(row) + str(feature_dict[row[1]])
    else:
        print ",".join(row) + str(float(0.0))



     
