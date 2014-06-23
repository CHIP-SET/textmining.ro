#!usr/local/python

import sys
import re

new_file = open(sys.argv[2], 'w')

frequency_flag =0
regex_letter = re.compile('[a-z]+')
regex_or = re.compile('\s?(or|to)\s?')
for line in open(sys.argv[1],'r'):
    if "dose_number" in line:
        new_file.write(line)
        continue
    boundary = line.find('.txt')
    txt = line[:boundary+5]
    frequency = line[boundary+5:].strip()
    regex_letter2 = re.search(regex_letter, frequency)
    regex_or2 = re.search(regex_or, frequency)
    if regex_letter2:
        if regex_or2:
            new_file.write(line)
            continue
        elif "hourly"==frequency or "hrly"==frequency or "hly"==frequency:
            new_file.write(line)
            continue            
        elif "oml"==frequency or "omls"==frequency:
            new_file.write(line)
            continue
        else:
            new_file.write(txt + "1"+ "\n")
    else:
        new_file.write(line)
new_file.close()
