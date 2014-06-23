
#!usr/local/python

import sys
import re

frequency_dose_file= open(sys.argv[2], 'w')

frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:5}{5:2}{6:5}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format('text_id','|','text', '|', 'DN_min','|','DN_MAX','|','DF_MIN','|','DF_MX','|','required?','|','DU','|','COD')+"\n")  

for line in open(sys.argv[1],'r'):
    if 'text_id' in line:
        continue      
    info = line.split('|')
    txt = info[0].strip()
    text = info[1].strip()
    dn_min = info[2].strip()
    dn_max = info[3].strip()
    df_min = info[4].strip()
    df_max = info[5].strip()
    required = info[6].strip()
    du = info[7].strip()
    cod = info[8].strip()
    if required == "yes": # if there is a required then the document frequency should be 0 since the patient may not take it :P
        #print info
        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(txt,'|',text, '|', dn_min,'|',dn_max,'|',"0",'|',df_max,'|',required,'|',du,'|',cod)+"\n")
    else:
        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(txt,'|',text, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod,'|')+"\n")  
frequency_dose_file.close()
