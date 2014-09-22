# coding:utf-8
# python submission_p_read_feature.py

from collections import defaultdict


def main():
    # probability
    userid_topicid2probability = defaultdict(lambda: defaultdict(float))
    # python user_topic.py > user_topic_p.txt
    fin = open("user_topic_p.txt", "r")
    for line in fin:
        try:
            user_id, topic_id, p_read, p_share = line.strip().split("\t")
            if not topic_id:
                topic_id = 0
            userid_topicid2probability[int(user_id)][float(topic_id)] = float(p_read)
        except:
            pass
    fin.close()
    # training_data
    fout = open("training_user_topic.csv", "w")
    fin = open("training_data.csv", "r")
    for line in fin:
        if "user_id" in line:
            fout.write('"user_id","on_cid","p_topic_id","type","created_at","feature"\n')
        elif ",," in line:
            fout.write(line.strip()+","+str(userid_topicid2probability[int(user_id)][float(p_topic_id)])+"\n")
        else:
            user_id, on_cid, p_topic_id, type_name, created_at = line.strip().split(",")
            if p_topic_id == '""':
                p_topic_id = 0
            fout.write(line.strip()+","+str(userid_topicid2probability[int(user_id)][float(p_topic_id)])+"\n")
    fin.close()
    fout.close()
    # submission_data
    fout = open("submission_user_topic.csv", "w")
    fin = open("submission_data_v2.csv", "r")
    for line in fin:
        if "user_id" in line:
            fout.write('"user_id","on_cid","p_topic_id","feature"\n')
        else:
            user_id, on_cid, p_topic_id = line.strip().split(",")
            if p_topic_id == '""':
                p_topic_id = 0
            fout.write(line.strip()+","+str(userid_topicid2probability[int(user_id)][float(p_topic_id)])+"\n")
    fin.close()
    fout.close()


if __name__ == '__main__':
    main()
