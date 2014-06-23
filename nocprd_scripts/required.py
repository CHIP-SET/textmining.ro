#!/usr/local/python

#author: george karystianis

import sys
import re

mega={}

for line in open(sys.argv[1],'r'):
    if "text_id" in line:
        continue
    txt = line.find('.txt')
    dosage_text = line.find('pr.')
    text_id = line[dosage_text+3:txt]
    mega[text_id] = text_id
    if "dose_unit\n"==line:
        break


new_file = open(sys.argv[3], 'w')
new_file.write("{0:7}{1:2}{2:70}{3:3}{4:10}{5:2}{6:10}{7:2}{8:}".format('text_id',' | ','text', ' | ', 'DN_min',' | ','DN_max', ' | ','required?')+"\n")  
for line in open(sys.argv[2],'r'): # here we open the file with the latest columns - 200columns.txt or 1000.columns,txt
    if "text_id" in line:
        continue
    info = line.split('|')
    line_id2=info[0].strip()
    text_info = info[1].strip().lower()
    extracted_dose_number_min=info[2].strip()
    extracted_dose_number_max=info[3].strip()
    if 'textid' in line:
        continue
    if line_id2 not in mega:
       # print line_id2
        if "as required" in text_info or "when required" in text_info or "if required" in text_info or "when needed" in text_info  or "if needed" in text_info or "as needed" in text_info or "pro re nata" in text_info or "sos" in text_info or "sit" in text_info or "siop" in text_info or "si opus sit" in text_info or "p.r.n" in text_info or "as reqd" in text_info or "when reqd" in text_info or "if reqd" in text_info or "as req" in text_info or "when req" in text_info or "if req" in text_info or "prn" in text_info or "p r n" in text_info or "p. r. n" in text_info or "when necessary" in text_info or "if necessary" in text_info or "as necessary" in text_info or "really necessary" in text_info or "absolutely necessary" in text_info:
            new_file.write("{0:7}{1:2}{2:70}{3:3}{4:11}{5:2}{6:11}{7:2}{8:}".format(line_id2,' | ',text_info,' | ', extracted_dose_number_min,'|',extracted_dose_number_max,'|','   yes')+"\n")
        else:
            new_file.write("{0:7}{1:2}{2:70}{3:3}{4:11}{5:2}{6:11}{7:8}{8:}".format(line_id2,' | ',text_info,' | ', extracted_dose_number_min,'|',extracted_dose_number_max,'|' ,'   no')+"\n")
    else:
        if "as required" in text_info or "when required" in text_info or "if required" in text_info or "when needed" in text_info  or "if needed" in text_info or "as needed" in text_info or "pro re nata" in text_info or "sos" in text_info or "sit" in text_info or "siop" in text_info or "si opus sit" in text_info or "p.r.n" in text_info or "as reqd" in text_info or "when reqd" in text_info or "if reqd" in text_info or "as req" in text_info or "when req" in text_info or "if req" in text_info or "prn" in text_info or "p r n" in text_info or "p. r. n" in text_info or "when necessary" in text_info or "if necessary" in text_info or "as necessary" in text_info or "really necessary" in text_info or "absolutely necessary" in text_info: 
         #   print line_id2
            new_file.write("{0:7}{1:2}{2:70}{3:3}{4:11}{5:2}{6:11}{7:2}{8:}".format(line_id2,' | ',text_info,' | ', extracted_dose_number_min,'|',extracted_dose_number_max,'|','   yes')+"\n")
        else:
            new_file.write("{0:7}{1:2}{2:70}{3:3}{4:11}{5:2}{6:11}{7:8}{8:}".format(line_id2,' | ',text_info,' | ', extracted_dose_number_min,'|',extracted_dose_number_max,'|' ,'   no')+"\n")
new_file.close()



