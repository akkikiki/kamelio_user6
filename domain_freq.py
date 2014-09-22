"""
python domain_freq.py contentsdata.csv training_data.csv domain_freq.dump

how to use dump file
import pickle
dic = pickle.load(open("domain_freq.dump"))
dic
 key = domain name
 val = freq (normalized)
"""

import sys
import csv
import re
import pickle

contentsdata = open(sys.argv[1])
traindata = open(sys.argv[2])
dump_file = sys.argv[3]

contents_reader = csv.reader(contentsdata)
train_reader = csv.reader(traindata)

re_digit = re.compile("[0-9]+")
re_domain = re.compile("//([^/]+)/")

docs = dict()

domain_freq = dict()

# get readed doc IDs 
for row in train_reader:
    if re_digit.match(row[0]):
        if "read" in row[3]:
            docs[row[1]] = docs.get(row[1], 0) + 1

# count domain name freq 
count = 0
for row in contents_reader:
    if re_digit.match(row[0]):
        if row[0] in docs:
            domain_name = re_domain.search(row[2]).group(1)
            domain_freq[domain_name] = domain_freq.get(domain_name, 0) + docs[row[0]]
            count += docs[row[0]]

# normalize freq
max_freq = max(val for val in domain_freq.values())
for key, val in domain_freq.items():
    domain_freq[key] = val*1.0/max_freq

# output
pickle.dump(domain_freq, open(dump_file, "w"))

contentsdata.close()
traindata.close()

