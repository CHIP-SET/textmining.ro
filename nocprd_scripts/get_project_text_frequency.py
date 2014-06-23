#!usr/local/python

import sys
import re

new_file = open(sys.argv[2], 'w')

frequency_flag =0
regex_letter = re.compile('[a-z]+')
regex_or = re.compile('\s?(or|to)\s?')
regex_hour = re.compile('([0-9])(?:-)?([0-9])?')
for line in open(sys.argv[1],'r'):
    if "dose_frequency" in line:
       frequency_flag = 1
       new_file.write(line)
    if frequency_flag == 1:
        boundary = line.find('.txt')
        txt = line[:boundary+5]
  #      print txt
        frequency = line[boundary+5:].strip()
        regex_letter2 = re.search(regex_letter, frequency)
        regex_or2 = re.search(regex_or, frequency)
        if regex_letter2:
            if regex_or2:
                new_file.write(line)
                continue
            elif "hourly"==frequency or "hrly"==frequency or "hly"==frequency or "hy"==frequency:
                new_file.write(line)
                continue            
            elif "oml"==frequency or "omls"==frequency:
                new_file.write(line)
                continue
            elif "q " in frequency:
                regex_hour2 = re.search(regex_hour, frequency)
                hour_1 = regex_hour2.group(1)
                hour_2 = regex_hour2.group(2)
                if str(hour_2)=="None":
                    dose_frequency = float(24)/float(hour_1)
                    if ".0" in str(dose_frequency):
                        dose_frequency = str(int(dose_frequency))
                    else:
                        dose_frequency = str(round(dose_frequency,1))
                    new_file.write(txt + dose_frequency + "\n")
                else:
                    dose_frequency_max = float(24)/float(hour_1)
                    dose_frequency_min = float(24)/float(hour_2)
                    if ".0" in str(dose_frequency_min):
                        dose_frequency_min = str(int(dose_frequency_min))
                    else:
                        dose_frequency_min = str(round(dose_frequency_min,1))
                    if ".0" in str(dose_frequency_max):
                        dose_frequency_max = str(int(dose_frequency_max))
                    else:
                        dose_frequency_max = str(round(dose_frequency_min,1))
                    new_file.write(txt + dose_frequency_min + "-" + dose_frequency_max + "\n")
 #                   print txt, dose_frequency_min, dose_frequency_max
            else:
             #   print line.strip()
                if frequency == "amount":
                 #   print line.strip()
                    new_file.write(txt + "?"+ "\n")
                else:
                  #  print frequency, txt
                    new_file.write(txt + "1"+ "\n")
        else:
            new_file.write(line)
