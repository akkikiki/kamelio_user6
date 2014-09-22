# coding: utf-8

# python script/extract_viewed_published_diff.py training_data.csv contentsdata.csv > training_data.csv_difftime_added 
import sys, codecs
import datetime
from datetime import date
import csv
import pandas as pd

f_doc = codecs.open(sys.argv[2], "r")
f_test = open(sys.argv[1], "r")

doc_info_dic = {}

reader = csv.reader(f_doc)


for columns in reader:
    #"contents_id","title","link","date_published","image_size"
    doc_info_dic[columns[0]] = columns[3] 

log_info_dic = {}
test_reader = csv.reader(f_test)

for columns in test_reader:
    #user_id, contents_id, p_topic_id, action_type, created_at =

    action_type = columns[3]
    contents_id = columns[1]
    user_id = columns[0]
    created_at = columns[-1]
    #log_info_dic[contents_id] = [created_at, user_id, action_type]

    if contents_id in doc_info_dic:
        #diff_date = user_article_difftime[key]
        diff_date = pd.to_datetime(created_at) - pd.to_datetime(doc_info_dic[contents_id])
        days, hours, minutes = diff_date.days, diff_date.seconds // 3600, diff_date.seconds // 60 % 60
        #diff_date = str(diff_date).replace(', ', '-')
        diff_date = str(days * 24 + hours)
        
        out_line = ",".join(columns) + "," + diff_date
        print out_line
    else:
        print ",".join(columns) + ","

