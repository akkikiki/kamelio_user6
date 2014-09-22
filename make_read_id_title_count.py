# coding:utf-8
import csv
from collections import defaultdict
#readされた記事のid,タイトル名,回数を出力


def main():
	training_data = open("training_data.csv","r")
	contents_data = open("contentsdata.csv","r")
	output_csv = open("id_title_readcount.csv","ab")
	train_read = csv.reader(training_data)
	contents_read = csv.reader(contents_data)

	read_id_count = defaultdict(int)


	for colums in train_read:
		if colums[3] == "article_read":
			read_id_count[colums[1]] += 1

	#print "read_id ", len(read_id)
	#print "contentsdata ", len(contents_read) 
	print "id_read",len(read_id_count.keys())

	contents_id_title = defaultdict(lambda :0)
	for colums in contents_read:
		contents_id_title[colums[0]] = colums[1]
	
	for id,count in read_id_count.items():
		#print id, contents_id_title[id],count
		csv.writer(output_csv).writerow([id,contents_id_title[id],count])
				
if __name__ == '__main__':
	main()