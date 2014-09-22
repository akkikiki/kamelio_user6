echo "条件付き確率ファイルを作成中... ファイル名 prob.txt"
python prob_show_read.py training_data.csv > prob.txt
echo "素性ファイル(人気度確率)を作成中... ファイル名 submission.prob.csv training_data.prob.csv"
python prob_feature.py prob.txt submission_data_v2.csv > submission.prob.csv
python prob_feature.py prob.txt training_data.csv > training_data.prob.csv
echo "素性ファイル(topic_id_feature)を作成中... ファイル名 traning.topic_id_feature.csv submission.topic_id_feature.csv"
python topic_id_feature.py training_data.csv training_data.csv > traning.topic_id_feature.csv
python topic_id_feature.py training_data.csv submission_data_v2.csv > submission.topic_id_feature.csv
