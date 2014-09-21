# coding:utf-8
# python submission_p_read.py > submission_p_read.csv

from collections import defaultdict


def main():
    # probability
    userid_topicid2probability = defaultdict(lambda: defaultdict(float))
    # python user_topic.py > user_topic_p.txt
    fin = open("user_topic_p.txt", "r")
    for line in fin:
        try:
            user_id, topic_id, p_read, p_share = line.strip().split("\t")
            userid_topicid2probability[user_id][topic_id] = float(p_read)
        except:
            pass
    fin.close()
    # submission_data
    fin = open("submission_data.csv", "r")
    for line in fin:
        if "user_id" in line:
            print '"user_id","on_cid","p_topic_id","Answer"'
        else:
            user_id, on_cid, p_topic_id = line.strip().split(",")
            if userid_topicid2probability[user_id][p_topic_id] > 0:
                print line.strip()+',"article_read"'
            else:
                print line.strip()+',"NULL"'
    fin.close()


if __name__ == '__main__':
    main()
