#coding:utf-8
#id_noun_set.dump,top_freq_title_noun_reg.csvから、各idに対してタイトルのスコアを作成
import csv,sys
import MeCab,re,math,pickle

def main():
	file1 = open("id_noun_set.dump","r")
	id_noun_set = pickle.load(file1)
	file2 = open("top_freq_title_noun_reg.dump","r")
	top_freq_noun = pickle.load(file2)
	output = open("id_titleScore","w")

	id_titleScore = {}

	for id,noun_set in id_noun_set.items():
		title_score = 0
		for noun in noun_set: #各ドキュメントのタイトル中の名詞
			try:
				if top_freq_noun[noun] > title_score: #最もスコアの高い名詞をスコアとしてとる
					title_score = top_freq_noun[noun]
			except:
				pass
		id_titleScore[id] = title_score

	pickle.dump(id_titleScore,output)

	#for k,v in id_titleScore.items():
	#	print k,v

	train_file = open("training_data.csv","r")
	train_out = open("training_data_title.csv","ab")
	train_reader = csv.reader(train_file)
	#csv.writer(train_out).writerow(["user_id","on_cid","p_topic_id","type","created_at","title"])
	for row in train_reader:
		try:
			title_score = float(id_titleScore[row[1]])
			row.append(title_score)
			csv.writer(train_out).writerow(row)
		except:
			pass

	submission_file = open("submission_data_v2.csv","r")
	submission_out = open("submission_data_v2_title.csv","ab")
	submission_reader = csv.reader(submission_file)
	csv.writer(submission_out).writerow(["user_id","on_cid","p_topic_id","title"])
	for row in submission_reader:
		try:
			title_score = float(id_titleScore[row[1]])
			row.append(title_score)
			csv.writer(submission_out).writerow(row)
		except:
			pass


if __name__ == '__main__':
	main()
