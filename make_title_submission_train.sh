echo "titleの数を計算...id_title_readcount.csv"
python make_read_id_title_count.py

echo "title中の名詞のtf値の計算"
python make_read_titlenoun_tf.py

echo "高頻度の名詞でゴミを除去"
cut_top_freq_title_noun.py

echo "idに対して名詞のセットを作成"
make_id_noun_set.py

echo "trainigとsubmissionのファイルを作成"
make_title_feature.py