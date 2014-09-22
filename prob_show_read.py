#!usr/bin/python
#coding:utf-8
"""
記事の人気度（P(read|show)の条件確率）の計算
python prob_show_read.py training_data.csv > prob.temp
"""
    
import sys
from collections import defaultdict

def prob_show_read():
    #記事ごとに辞書を作成
    #{article_id, {}}
    article_dict = defaultdict(lambda:defaultdict(lambda:0))    
            
    training_file = open(sys.argv[1])
    training_file.readline()
    #article_show, article_read, article_shareカウント
    for line in training_file:
        itemList = line.strip().split(',')
        if itemList[3] == '"article_show"':
            article_dict[itemList[1]]["article_show"] += 1
        if itemList[3] == '"article_read"':
            article_dict[itemList[1]]["article_read"] += 1
        if itemList[3] == '"article_share"':
            article_dict[itemList[1]]["article_share"] += 1

#    for on_cid, value in article_dict.items():
#        print on_cid, value["article_show"], value["article_read"]

    #確率の計算
    for on_cid, value in article_dict.items():
        #0確率の分母になる"article_show"の頻度が0である場合を回避
        if article_dict[on_cid]["article_show"] != 0: #確率の分母になる"article_show"の頻度が0である場合を回避
            article_dict[on_cid]["prob"] = float(value["article_read"])/\
                                            article_dict[on_cid]["article_show"]
    #出力
    for on_cid, value in article_dict.items():
        if on_cid != "":
            print on_cid, value["prob"]

if __name__ == "__main__":
    prob_show_read()
