#!/usr/local/python

#author: george karystianis

import sys
import re

new_file = open(sys.argv[3],'w')
mega={}
mega2={}

for line in open(sys.argv[1],'r'):
    if "dose_number" in line:
        continue
    if "amount\n" == line:
        break
    boundary = line.find('pr.')
    boundary2 = line.find('.txt')
    line_id=line[boundary+3:boundary2]
    dose_number_min = line[boundary2+5:].strip()
    dose_number_max = dose_number_min
    regex= re.compile('([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:or|-|to)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)')
    regex2= re.compile('([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:/)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)')
    hello = re.search(regex, line)
    hello2 = re.search(regex2, line)
    if hello:
        dose_number_min = str(hello.group(1))
        dose_number_max = str(hello.group(2))
        if float(dose_number_min) > float(dose_number_max):
            new_dose_number_min = dose_number_max
            new_dose_number_max = dose_number_min
            dose_number_min = new_dose_number_min
            dose_number_max = new_dose_number_max
    dose_number_min = str(dose_number_min)
    dose_number_max = str(dose_number_max)
    if hello2:
        dose_number_min= float(hello2.group(1)) / float(hello2.group(2))
        dose_number_min = str(round(dose_number_min,1))
        dose_number_min = dose_number_min
        dose_number_max = dose_number_min
    dose_number_min = str(dose_number_min)
    dose_number_max = str(dose_number_max)
    if ".0" in dose_number_min: ## this is to do 2.0 into 2 so we wont lose true positives
        dose_number_min = int(round(float(dose_number_min)))
        dose_number_min = str(dose_number_min)
        dose_number_min = dose_number_min
        dose_number_max = dose_number_min
        mega[line_id] = dose_number_min
        mega2[line_id] = dose_number_max
    else:
        mega[line_id] = dose_number_min
        mega2[line_id] = dose_number_max

new_file.write("{0:7}{1:2}{2:70}{3:3}{4:16}{5:2}{6:}".format('text_id',' | ','text', ' | ', 'DN_min','|','DN_max')+"\n")  
for line in open(sys.argv[2],'r'):
    info = line.split('\t')
    # i can get the elements from here. now i am focusing on the second column
    #dose_number2 = info[3].strip()
    line_id2=info[0]
    text_info = info[1].strip('"').strip('"\n')
    print text_info
    if 'textid' in line:
        continue
    if line_id2 not in mega:
        new_file.write("{0:7}{1:2}{2:70}{3:3}{4:16}{5:2}{6:}".format(line_id2,' | ',text_info, ' | ', '?','|','?')+"\n")
    else:
     #   print line
        new_file.write("{0:7}{1:2}{2:70}{3:3}{4:16}{5:2}{6:}".format(line_id2,' | ',text_info, ' | ', mega[line_id2],'|',mega2[line_id2])+"\n")         
new_file.close()
