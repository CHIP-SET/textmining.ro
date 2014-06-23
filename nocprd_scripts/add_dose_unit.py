#!usr/local/python

#author: george karystianis
#date: 7/11/2012
#this is a scrip that extends the columns already and adds an extract column about the dosage unit.

import sys
import re

new_file = open(sys.argv[3],'w')
mega={} #open the extracted_medinfo[number].txt

dose_unit_flag=0
for line in open(sys.argv[1],'r'):
    if "dose_unit\n"==line:
        dose_unit_flag = 1
        continue
    if dose_unit_flag==1:
        txt = line.find('.txt')
        dosage_text = line.find('pr.')
        text_id = line[dosage_text+3:txt]
        dose_unit = line[txt+5:].strip()
        mega[text_id] = dose_unit
    if "dose_frequency\n"==line:
        break

new_file.write("{0:7}{1:2}{2:70}{3:2}{4:5}{5:2}{6:5}{7:2}{8:8}{9:2}{10:}".format('text_id','|','text', '|', 'DN_min','|','DN_max', '|' ,'required?', '|','dose_unit')+"\n")  

 
for line in open(sys.argv[2],'r'): # here we open the file with the latest columns - new_[number]columns.txt or [number].columns,txt
    if "text_id" in line:
        continue
    info = line.split('|')
    line_id2=info[0].strip()
    text_info = info[1].strip()
    extracted_dose_number_min=info[2].strip()
    extracted_dose_number_max = info[3].strip()
    required = info[4].strip()
    if 'textid' in line:
        continue
    if line_id2 not in mega:
       # print line
        new_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:}".format(line_id2,'|',text_info,'|', extracted_dose_number_min,'|',extracted_dose_number_max,'|',required,'|','-')+"\n")
    else:
        if mega[line_id2]=="":   
            mega[line_id2] == "-"
        if mega[line_id2] == "tablet" or mega[line_id2] == "tablets" or mega[line_id2]=="tabs" or mega[line_id2]=="tabweekly" or mega[line_id2]=="tabtds" or mega[line_id2]=="tabod" or mega[line_id2]=="tabbd" or mega[line_id2]=="tabnocte" or mega[line_id2]=="tabmane" or mega[line_id2]=="tabdaily" or mega[line_id2]=="tabd":
            mega[line_id2] = "tab"
        if mega[line_id2] == "capsule" or mega[line_id2] == "caps" or mega[line_id2]=="capsules" or mega[line_id2] == "capbd" or mega[line_id2] == "captid" or mega[line_id2] == "captds" or mega[line_id2] == "capnocte" or mega[line_id2] == "capdaily" or mega[line_id2]=="capqds":
            mega[line_id2] = "cap"    
        if mega[line_id2] == "sachets" or mega[line_id2] == "sachetbd":
            mega[line_id2] = "sachet"
        if mega[line_id2] == "pastilles":
            mega[line_id2] = "pastille"
        if mega[line_id2] == "pills":
            mega[line_id2] = "pill"
        if mega[line_id2] == "drops" or mega[line_id2] == "dr" or mega[line_id2]=="drp" or mega[line_id2]=="drps":
            mega[line_id2] = "drop"
        if mega[line_id2] == "puffs" or mega[line_id2] =="pufs" or mega[line_id2]=="puf":
            mega[line_id2] = "puff"
        if mega[line_id2] == "blisters":
            mega[line_id2] = "blister"
        if mega[line_id2] == "amps" or mega[line_id2] == "ampoule" or mega[line_id2]=="ampoules":
            mega[line_id2] = "amp"
        if mega[line_id2] == "sprays" or mega[line_id2] == "spr" or mega[line_id2] == "sprayys" or mega[line_id2] == "spraybd" or mega[line_id2] == "sprayqds":
            mega[line_id2] = "spray"
        if mega[line_id2] == "mls" or mega[line_id2] == "milliliters" or mega[line_id2] == "milliliters" or mega[line_id2] == "millilitre" or mega[line_id2] =="millilitres" or mega[line_id2] =="msl":
            mega[line_id2] = "ml"
        if mega[line_id2] == "g" or mega[line_id2] == "gm" or mega[line_id2] == "gms" or mega[line_id2] == "grams":
            mega[line_id2] = "gram"
        if mega[line_id2] == "micrograms" or mega[line_id2] == "mcgs" or mega[line_id2] == "micro grams" or mega[line_id2] == "micro gram" or mega[line_id2] == "microgram" or mega[line_id2] == "mcgqds":
            mega[line_id2] = "mcg"
        if mega[line_id2] == "mgs" or mega[line_id2] == "mg" or mega[line_id2] == "milligram" or mega[line_id2] == "milli gram" or mega[line_id2] == "milligrams" or mega[line_id2] == "milli grams" or mega[line_id2] == "mgbd" or mega[line_id2] == "mgtds" or mega[line_id2] == "mgod" or mega[line_id2] == "mgqds" or mega[line_id2] == "mgdaily" or mega[line_id2] == "mgswkly" or mega[line_id2] == "mgom" or mega[line_id2] == "mgnocte" or mega[line_id2] == "mgms" or mega[line_id2] == "mgm":
            mega[line_id2] = "mg"
        if mega[line_id2] == "suppositor" or mega[line_id2] == "suppository":
            mega[line_id2] = "suppos"
        if mega[line_id2] == "vials":
            mega[line_id2] = "vial"
        if mega[line_id2] == "patches":
            mega[line_id2] = "patch"
        if mega[line_id2] == "ounces":
            mega[line_id2] = "ounce"
        if mega[line_id2] == "units":
            mega[line_id2] = "unit"
        if mega[line_id2] == "lozenge" or mega[line_id2] == "lozenges" or mega[line_id2] == " losenges":
            mega[line_id2] = "losenge"
        if mega[line_id2] == "packs" or mega[line_id2] == "packets" or mega[line_id2] == " packet":
            mega[line_id2] = "pack"
        if mega[line_id2] == "capfuls" or mega[line_id2] == "capfulls" or mega[line_id2] == "capful":
            mega[line_id2] = "capfull"
        if mega[line_id2] == "":
            mega[line_id2] = "-"
        new_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:}".format(line_id2,'|',text_info,'|', extracted_dose_number_min,'|',extracted_dose_number_max,'|',required,'|', mega[line_id2])+"\n")     
new_file.close()
