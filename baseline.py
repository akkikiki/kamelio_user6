
import sys

f_input = open(sys.argv[1], 'r')
f_out = open(sys.argv[1] + "_out", 'w')
#"user_id","on_cid","p_topic_id"
first_line = f_input.readline()
first_line_out = str(first_line[:-1]) + ',"Answer"\n'
f_out.write(first_line_out)

for line in f_input:
    f_out.write(line[:-1] + ",article_read\n")
