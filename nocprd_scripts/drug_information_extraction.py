#!/usr/local/python

#this is a script which fetches the text from common dosages and returns the text only. Purpose of this is to separate each line into a different file so we can 
# perform minorthird into ease.

#it seems that filtering should be done here as we will avoid cases 

import sys

text_file = open(sys.argv[3],'w')
stop_list = []
unique = {}

stoplist = open(sys.argv[2],'r')
for line in stoplist:
    stop_list.append(line.strip())

count = 0
text_with_information = 0
total_duplicates = 0
unique_noise = 0
#extra_noise = 0
#clean_duplicates = 0
for line in open(sys.argv[1],'r'):
    if line =="textid	text	daily_dose	dose_number	dose_unit	dose_frequency	dose_interval	choice_of_dose	dose_max_average	change_dose	dose_duration\n":
        continue
    boundary=line.find('"')
    text = line[boundary+1:]
    text_id = line[:boundary].strip()
    boundary2=text.find('"')
    clean_text = text[:boundary2]
    splitted_line = line.split('\t')
    dose_unit = splitted_line[4]
    dose_unit = dose_unit.strip('"')
    if clean_text not in unique:
        unique[clean_text] = ""
        count = count + 1
        if clean_text not in stop_list:
            text_with_information = text_with_information + 1
            clean_text = clean_text.lower()
            text_file2 = open(sys.argv[3]+"."+text_id+".txt", 'w')
            text_file2.write(text_id+ " thisisthebeginning "+ clean_text+"\n")
            text_file2.close()
        else:
            unique_noise = unique_noise + 1
            continue
#            print clean_text
    else:
        total_duplicates = total_duplicates + 1
#        if "~~" not in clean_text:
 #           text_with_information = text_with_information + 1
  #          clean_text = clean_text.lower()
   #         text_file2 = open(sys.argv[2]+"."+text_id+".txt", 'w')
    #        text_file2.write(text_id+ " thisisthebeginning "+ clean_text+"\n")
     #       text_file2.close()
    #    else:
   #         unique_noise = unique_noise + 1
  #          print clean_text
 #   else: # this is for the duplciates - perhaps they want them since each file is kinda unique - assigned to different patient
       # if clean_text not in stop_list:
  #      total_duplicates = total_duplicates+ 1
   #     if "~~" not in clean_text:
    #        clean_duplicates = clean_duplicates + 1
     #       text_with_information = text_with_information + 1
      #      clean_text = clean_text.lower()
       #     text_file2 = open(sys.argv[2]+"."+text_id+".txt", 'w')
        #    text_file2.write(text_id+ " thisisthebeginning "+ clean_text+"\n")
         #   text_file2.close()
       # else:
        #    extra_noise = extra_noise + 1        
text_file2.close()
print "prescriptions: ", count
print "filtered prescriptions: ", text_with_information
print "total duplicates: ", total_duplicates
#print "clean duplicates: ", clean_duplicates
print "unique noise: ", unique_noise
#print "extra noise:" , extra_noise
