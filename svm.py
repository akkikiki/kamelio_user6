# coding:utf-8

import sys
sys.path.append("/Users/kajiwaratomoyuki/Dropbox/yakinikublog/aozora_analize/libsvm-3.17/python")
from svm import *
from svmutil import *


def get_labels():
    label_list = []
    fin = open("training_data.csv", "r")
    for line in fin:
        if "user_id" in line:
            continue
        user_id, on_cid, p_topic_id, type_name, created_at = line.strip().split(",")
        if "read" in line or "share" in line:
            label_list.append(1)
        else:
            label_list.append(-1)
    fin.close()
    return label_list


def get_features(fname, feature_list):
    fin = open(fname, "r")
    for i, line in enumerate(fin):
        if "user_id" in line:
            continue
        i = i - 1
        feature = line.strip().split(",")[-1]
        try:
            feature_list[i].append(float(feature))
        except:
            feature_list.append([float(feature)])
    fin.close()
    return feature_list


def main():
    label_list = get_labels()
    training_feature_list = []
    test_feature_list = []
    for fname in sys.argv[1:]:
        if "training" in fname:
            training_feature_list = get_features(fname, training_feature_list)
        elif "submission" in fname:
            test_feature_list = get_features(fname, test_feature_list)
    problem = svm_problem(label_list, training_feature_list)
    parameter = svm_parameter()
    model = svm_train(problem, parameter)
    predict_labels, accuracy, values = svm_predict(label_list, test_feature_list, model)
    svm_save_model("test.model", model)
    print predict_labels


if __name__ == '__main__':
    main()
