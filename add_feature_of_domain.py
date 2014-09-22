"""
if you use this script, you must created domain_freq.dump by domain_freq.py

python add_feature_of_domain.py (submission_data_v2.csv or training_data.csv) contentsdata.csv domain_freq.dump 
"""
import sys
import pickle
import re
import csv

submitdata = open(sys.argv[1])
contentsdata = open(sys.argv[2])
domain_freq = pickle.load(open(sys.argv[3]))

submit_reader = csv.reader(submitdata)
contents_reader = csv.reader(contentsdata)

re_digit = re.compile("[0-9]+")
re_domain = re.compile("//([^/]+)/")
re_domain2 = re.compile("//(.*)")

# doc2freq
d2f = dict()
for row in contents_reader:
    if re_digit.match(row[0]):
        if not re_domain.search(row[2]):
            domain_name = re_domain2.search(row[2]).group(1)
        else:
            domain_name = re_domain.search(row[2]).group(1)
        d2f[row[0]] = domain_freq.get(domain_name, 0)

# domain_name
for row in submit_reader:
    if row[0] == 'user_id':
        print '"'+'","'.join(row)+'","domain_freq"'
        continue
    print ",".join(row)+","+str(d2f.get(row[1], 0))

submitdata.close()
contentsdata.close()

