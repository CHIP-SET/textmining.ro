#!/usr/local/python


##this is a script that checks if I have any word in the columns :P

import sys
import re

#1      | take one daily                                                        | 1     | 1     | 1       | 1       | 1       | 1       | no       | -         | 0

for line in open(sys.argv[1], 'r'):
    if "--------------" in line:
        continue
    info = line.split('|')
    txt_id = info[0]
    txt = info[1]
    dn_min = info[2]
    dn_max = info[3]
    df_min = info[4]
    df_max = info[5]
    di_min = info[6]
    di_max = info[7]
    regex_letter = re.compile('[a-z]')
    regex_double_number = re.compile('[0-9]\s[0-9]')
    regex_letter_dn_min = re.search(regex_letter, dn_min)
    regex_letter_dn_max = re.search(regex_letter, dn_max)
    regex_letter_df_min = re.search(regex_letter, df_min)
    regex_letter_df_max = re.search(regex_letter, df_max)
    regex_letter_di_min = re.search(regex_letter, di_min)
    regex_letter_di_max = re.search(regex_letter, di_max)
    regex_double_number_dn_min = re.search(regex_double_number, dn_min)
    regex_double_number_dn_max = re.search(regex_double_number, dn_max)
    regex_double_number_df_min = re.search(regex_double_number, df_min)
    regex_double_number_df_max = re.search(regex_double_number, df_max)
    regex_double_number_di_min = re.search(regex_double_number, di_min)
    regex_double_number_di_max = re.search(regex_double_number, di_max)

    if regex_letter_dn_min or regex_letter_dn_max or regex_letter_df_max or regex_letter_df_max:
        print line.strip()
    if regex_double_number_dn_min or regex_double_number_dn_max or regex_double_number_df_max or regex_double_number_df_max: 
        print line.strip() 
    if regex_letter_di_min or regex_letter_di_max:
        if "month" in di_min:
            continue
        else:
            print line.strip()
    if regex_double_number_di_min or regex_double_number_di_max: 
        print line.strip() 

