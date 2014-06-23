#!usr/local/python

#author: george karystianis
#date: 2/11/2012

import sys

#get_me = open(sys.argv[2],'w')

f = open(sys.argv[1])
lines = f.readlines()
f.close()

n = len(lines)
info_list = []

for i in range(1, n):
    org_line = lines[i]
    boundary=org_line.find('"')
    text = org_line[boundary+1:]
    text_id = org_line[:boundary].strip()
    boundary2=text.find('"')
    clean_text = text[:boundary2]
    for j in range (i+1, n):
        cmp_line = lines[j]
        boundary=cmp_line.find('"')
        text = cmp_line[boundary+1:]
        text_id = cmp_line[:boundary].strip()
        boundary2=text.find('"')
        new_text = text[:boundary2]
        if new_text not in info_list:
            if new_text == clean_text:
               # get_me.write(org_line)
                #get_me.write(cmp_line)
                info_list.append(new_text)
                print org_line
                print "---------------------"
                print cmp_line
#get_me.close()
