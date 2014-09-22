"""
python add_feature_of_hatebu.py contentsdata.csv training_data.csv > train.hatebu
python add_feature_of_hatebu.py contentsdata.csv submission_data_v2.csv > submission.hatebu
"""
import sys
import re
import csv
from urllib import urlopen

contentsdata = open(sys.argv[1])
traindata = open(sys.argv[2])
reader = csv.reader(contentsdata)
treader = csv.reader(traindata)

re_digit = re.compile("[0-9]+")

# d2h
d2h = dict()
for row in reader:
    num = "0"
    if re_digit.match(row[0]):
        num = urlopen("http://api.b.st-hatena.com/entry.count?url="+row[2]).read()
        if num="":
    num="0"
        d2h[row[0]] = int(num)


for row in train_reader:
    if row[0] == "user_id":
        print '"'+'","'.join(row)+'","hatebu"'
        continue
    else:
        print ",".join(row)+","+str(d2h.get(row[1], 0))



contentsdata.close()
traindata.close()

