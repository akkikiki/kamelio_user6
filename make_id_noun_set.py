#coding:utf-8
import csv
import MeCab,re,math,pickle
#コンテンツデータから、idに対して、タイトルの名詞のセットの組を出力

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

def main():
	f = open("contentsdata.csv","r") 
	output = open("id_noun_set.dump","w")
	reader = csv.reader(f)
	id_noun_set = {}
	for row in reader:
		text = row[1].decode("utf-8")
		noun = getNoun(text)
		id_noun_set[row[0]] = noun
		#print row[0], " ".join(noun)

	pickle.dump(id_noun_set,output)




if __name__ == '__main__':
	main()