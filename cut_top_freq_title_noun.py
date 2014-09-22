#coding:utf-8
#top_freq_title_noun.csvからゴミを取り除く

import csv

def main():
	f = open("top_freq_title_noun.csv","r")
	cut_nouns = {}
	reader = csv.reader(f)
	for row in reader:
		try:
			#print row[0].decode("utf-8")
			if not len(row[0].decode("utf-8")) == 1:
				cut_nouns[row[0]] = int(row[1])
				#print row[0],row[1]
		except:
			pass
	max_freq = float(max(cut_nouns.values())) #最大頻度
	for k in cut_nouns.keys():
		cut_nouns[k] = cut_nouns[k] / max_freq
		print k, cut_nouns[k]
	#print max_freq





if __name__ == '__main__':
	main()