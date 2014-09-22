#coding:utf-8
import csv
import MeCab,re,math
#タイトルに頻出する名詞、回数を昇順に出力

def getNoun(words):
   noun = []
   tagger = MeCab.Tagger( "-Ochasen" )
   node = tagger.parseToNode( words.encode( "utf-8" ) )
   while node:
      if node.feature.split(",")[0] == "名詞":
         replace_node = re.sub( re.compile( "[!-/:-@[-`{-~]" ), "", node.surface )
         if replace_node != "" and replace_node != " ":
            noun.append( replace_node )
      node = node.next
   return noun

def getTopKeywords(TF,n):
   list = sorted( TF.items(), key=lambda x:x[1], reverse=True )
   return list[0:n]

def calcTFIDF( N,TF, DF ):
   tfidf = TF * math.log( N / DF )
   return tfidf

def main():
	tf = {}
	df = {}
	f = open("id_title_readcount.csv","r") #id,タイトル,readの回数がcsvに格納されたもの。
	reader = csv.reader(f)
	N = 0
	for row in reader:
		N += int(row[2])
		df_list = []
		text = row[1].decode("utf-8")
		noun = getNoun(text)
		#print " ".join(noun)
		for word in noun:
			try:
				tf[word] = tf[word] + 1*int(row[2])
			except KeyError:
				tf[word] = 1*int(row[2])
		"""
		for word in noun:
			try:
				if word in df_list: 
					continue
				df[word] = df[word] + 1*int(row[2])
			except KeyError:
				df[word] = 1*int(row[2])
		"""
	tfidf = {}
	for k,v in getTopKeywords( tf, 100 ):
		#tfidf[k] = calcTFIDF(N,tf[k],df[k])
		print k,v
	"""
	for k,v in getTopKeywords( tfidf, 100):
		print k,v
	"""



if __name__ == '__main__':
	main()