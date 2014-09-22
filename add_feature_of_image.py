"""
python add_feature_of_image.py contentsdata.csv training_data.csv > train.imagesize
python add_feature_of_image.py contentsdata.csv submission_data_v2.csv > submission.imagesize
"""
import sys
import csv
import re

contentsdata = open(sys.argv[1])
traindata = open(sys.argv[2])

contents_reader = csv.reader(contentsdata)
train_reader = csv.reader(traindata)

re_digit = re.compile("[0-9]+")

#doc2imagesize
d2i = dict()
for row in contents_reader:
    if re_digit.match(row[0]):
        if row[-1]:
            if row[-1]!="[]":
                images = row[-1][2:-2].split("], [")
                size = max(map(lambda x: int(x.split(", ")[0])*int(x.split(", ")[1]), images)) 
                d2i[row[0]] = size

max_size = max(d2i.values())
# normalize
for key, value in d2i.items():
    d2i[key] = value*1.0/max_size

for row in train_reader:
    if row[0] == "user_id":
        print '"'+'","'.join(row)+'","image_size"'
        continue
    else:
        print ",".join(row)+","+str(d2i.get(row[1], 0))

contentsdata.close()
traindata.close()

