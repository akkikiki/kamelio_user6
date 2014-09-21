# coding:utf-8
# python user_topic.py > user_topic_p.txt

from collections import defaultdict


def main():
    # user_id
    user_id2freq = defaultdict(int)
    # cut -d"," -f1 training_data.csv | sort | uniq -c > user_article.txt
    fin = open("user_article.txt", "r")
    for line in fin:
        freq, user_id = line.strip().split(" ")
        user_id2freq[user_id] = int(freq)
    fin.close()
    # user_id, topic, type
    user_id2topic = defaultdict(set)
    user_id2read_freq = defaultdict(lambda: defaultdict(int))
    user_id2share_freq = defaultdict(lambda: defaultdict(int))
    # cut -d"," -f1,3,4 training_data.csv | sort | uniq -c > user_topic_type.txt
    fin = open("user_topic_type.txt", "r")
    for line in fin:
        line = line.strip().split(" ")
        freq = line[0]
        user_id, topic_id, type_name = line[1].split(",")
        user_id2topic[user_id].add(topic_id)
        if "read" in type_name:
            user_id2read_freq[user_id][topic_id] = int(freq)
        elif "share" in type_name:
            user_id2share_freq[user_id][topic_id] = int(freq)
    fin.close()
    # for
    print "user_id\ttopic_id\tp_read\tp_share"
    for user_id in user_id2freq.keys():
        for topic_id in user_id2topic[user_id]:
            p_read = float(user_id2read_freq[user_id][topic_id])/float(user_id2freq[user_id])
            p_share = float(user_id2share_freq[user_id][topic_id])/float(user_id2freq[user_id])
            print str(user_id)+"\t"+str(topic_id)+"\t"+str(p_read)+"\t"+str(p_share)


if __name__ == '__main__':
    main()
