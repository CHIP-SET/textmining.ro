#!usr/local/python

#author: george karystianis
#date: 4/12/12
#comments: this is a script that incorporates the choice of dose column to the already expanded column schema of the rest :P and makes comparison while calculating what is correct and incorrect.

import sys
mega = {}
mega2 = {}
mega3 = {}

new_file = open(sys.argv[3],'w')

for line in open(sys.argv[1],'r'):  
    if "textid" in line:
        continue
    info = line.split('|')
    text_id=info[0].strip().strip()
    extracted_choice_of_dose =info[2].strip()
    mega[text_id] = extracted_choice_of_dose

new_file.write("{0:7}{1:2}{2:70}{3:2}{4:5}{5:2}{6:5}{7:2}{8:8}{9:2}{10:7}{11:2}{12:}".format('text_id','|','text', '|', 'DN_min','|','DN_max','|','required?', '|','dose_unit','|','COD')+"\n") 

for line in open(sys.argv[2],'r'): 
    if 'text_id' in line:
        continue
    line = line.strip()
    info = line.split('|')
    line_id=info[0].strip()
    text_info = info[1].strip()
    extracted_dose_number_min = info[2].strip()
    extracted_dose_number_max = info[3].strip()
    required = info[4].strip()
    dosage_unit = info[5].strip()
  #  new_line = line + mega[line_id]
   # print line
    new_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:7}{11:2}{12:}".format(line_id,'| ',text_info, '|', extracted_dose_number_min,'|',extracted_dose_number_max, '|',required, '|',dosage_unit,'|',mega[line_id])+"\n") 
new_file.close()
