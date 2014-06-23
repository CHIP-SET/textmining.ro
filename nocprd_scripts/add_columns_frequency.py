#author: george karystianis

#date: 19/11/2012

#this is a script that scans the original text of the medical prescriptions and extracts the choice of dose - either being o, 1 or 2 maximum

import sys
import re

mega={}
mega2 = {}
mega3 = {}

frequency_dose_file= open(sys.argv[3], 'w')

frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:5}{5:2}{6:5}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format('text_id','|','text', '|', 'DN_min','|','DN_MAX','|','DF_MIN','|','DF_MX','|','required?','|','DU','|','COD')+"\n")  

for line in open(sys.argv[1],'r'): # this is reading the columns and frequency[number] file.
    if 'text_id' in line:
        continue
    info = line.split('|')
    txt_id = info[0].strip()
    df_min = info[2].strip()
    df_max = info[3].strip()
    mega[txt_id] = df_min
    mega2[txt_id] = df_max

for line in open(sys.argv[2],'r'):  # this is reading the all columns together[number] file
    if 'text_id' in line:
        continue      
    info = line.split('|')
    line_id = info[0].strip()
    information = info[1].strip()
    dn_min = info[2].strip()
    dn_max = info[3].strip()
    required = info[4].strip()
    dose_unit = info[5].strip()
    cod = info[6].strip()
    frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(line_id,'|',information, '|', dn_min,'|',dn_max,'|',mega[line_id],'|',mega2[line_id],'|',required,'|',dose_unit,'|',cod)+"\n")  
frequency_dose_file.close()
