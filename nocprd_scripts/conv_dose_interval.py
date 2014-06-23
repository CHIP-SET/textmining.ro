#!usr/local/python

import sys
import re

new_extracted_dose_interval = open(sys.argv[2], 'w')

number_dict={"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "ten":"10", "eleven":"11", "twelve":"12", "third": "3", "fourth":"4", "fifth":"5", "sixth":"6", "seventh":"7", "eight":"8", "ninth":"9", "tenth":"10", "other":"2", "second":"2", "first":"1", "alternate":"2", "alt":"2", "at":"1"}

def convert(n): #function that converts a word number into a number when it is called :P
    if n in number_dict:
        return number_dict[n]
    else:
        return n

regex_multiple_days = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(?:-|to|or|\/)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(?:alt|alternate|other|dieb\salt)?(?:\s+)?(?:.)?(?:\s+)?(?:days|day|nights|night)')

regex_multiple_weeks = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(?:-|to|or|\/)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)(?:alt|alternate|other|dieb\salt)?(?:\s+)?(?:.)?(?:\s+)?(?:weeks|week|wks|wk)')

regex_multiple_months = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(?:-|to|or|\/)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)(?:alt|alternate|other|dieb\salt)?(?:\s+)?(?:.)?(?:\s+)?(?:months|month)')

regex_multiple_year =re.compile('([0-9]+)(?:\s+)?(?:-|\/|to|or)?\s?([0-9]+)(?:\s+)?(?:alt|alternate|other|dieb\salt)?(?:\s+)?(?:.)?(?:\s+)?(years|year|yr)')

regex_weird_weeks = re.compile('(once)(?:\s+)?(?:-|to|or)(?:\s+)?(twice)(?:\s+)?(?:per|every|each|a|the|in\sthe)?(?:\s+)(?:weeks|week|wks|wk|weekly|wkly|wly)')

regex_aday = re.compile('(at|during|in|every|each|a|an|per)(?:\s+)?(the)?(?:\s+)?(day|eve|evening|morne|morning|morn|midnight|night|bedtime|teatime|tea\stime|dawn|dinner\stime|noon|dusk|afternoon|noct|nocte|mane|lunchtime|lunch\stime|dinner\stime|dinnertime|noc)')

regex_meansdaily = re.compile('daily|dly|nightly|times\s?/\s?day|mane|opd|o.p.d|qam|q.a.m|qds|q.d.s|nocte|om|o.m|on\Z|o.n|qpm|q.p.m|qd|q.d|q1d|q.1.d|sid|s.i.d|q.i.d|qid|tds|t.d.s|qh|q.h|qhs|q.h.s|q1h|q.1.h|q2h|q.2.h|q3h|q.3.h|q4h|q.4.h|q5h|q.5.h|q6h|q.6.h|q7h|q.7.h|q8h|q.8.h|q9h|q.9.h|q10h|q11h|q12h|q.11.h|q.12.h|q.10.h|q1|q2|q3|q4|q5|q6|q7|q8|q9|q10|q11|q12|qqh|q.q.h|am\Z|a.m|pm|p.m|bd|b.d|tid|td|q3h|q4h|q5h|q6h|q7h|q8h|q.3.h|q.4.h|q.5.h|q.6.h|q.7.h|q.8.h|q.3.h.|q.4.h.|q.5.h.|q.6.h.|q.7.h.|q.8.h.|b.\s?d.|t.\s?d.\s?s|t\si\sd')

regex_52 = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(?:\/)(?:\s+)?(?:52)')

regex_12 = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(?:\/)(?:\s+)?(?:12)')

regex_7 = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(?:\/)(?:\s+)?(?:7)')

regex_every_day = re.compile('(?:every|each)(?:\s+)?([2-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(?:day|days|nights|night)')

regex_every_week = re.compile('(?:every|each)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(?:weeks|week|wk|wks)')

regex_every_month = re.compile('(?:every|each)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(?:months|monthly|mthly|month)')

regex_every_day_or = re.compile('(?:every|each)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?()(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(?:day|days)')

regex_month = re.compile('a\smonth|monthly|mnthly|mthly')

regex_week = re.compile('(a|per|the)?(?:\s+)?(week|weekly|wkly|wly|weeks|wks|tiw|t.i.w|qwk|q.w.k)')

regex_hours = re.compile('(?:every)(?:\s+)?([2-9][0-9])(?:\s+)?(hours|hrs|hr|hour)')

regex_number_month = re.compile('([0-9]|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)(?:\s+)?(month|monthly|mnthly|mthly|months)')

regex_other_day = re.compile('(every|each)?(?:\s+)?(other)(?:\s+)?|(alt|dieb.\salt.|dieb\salt|eod|e.o.d|q.a.d|qad|alt)(?:\s+)?(day|eve|evening|morne|morning|morn|midnight|night|bedtime|teatime|tea\stime|dinner\stime|dawn|noon|dusk|afternoon|noct|nocte|mane|lunchtime|lunch\stime|dinner\stime|dinnertime|noc)')

#alt_timeunits_single = re.compile('([0-9]+)\s?(days|day|nights|night|years|year|months|month|yr|weeks|week|wk|wks)')

regex_times = re.compile('(?:[a-z]|[0-9]+|[0-9].[0-9])(?:\s+)?(?:times)(?:\s+)?(?:/|a|per)?(?:\s+)?(day)')

regex_on = re.compile('[0-9]\s?(-|to|or)?\s?[0-9]?\s?(on\Z)')

def comp(x,y):
    if int(x) > int(y):
        line = y + "-" + x
        return line
    elif int(y) > int(x):
        line =x + "-" + y
        return line
    else:
        line = x + "-" + x
        return line 

interval_flag=0
for line in open(sys.argv[1],'r'): # here you are opening the extracted information from minorthird
    line = line.strip()
    if "dose_interval" in line:
        interval_flag = 1
        new_extracted_dose_interval.write("dose_interval"+"\n")
        continue
    if interval_flag==1:
     #   print line.strip()
        txt = line.find('.txt')
        txt_id = line[:txt+4].strip()
        info = line[txt+5:].strip()
        regex_multiple_days2 = re.search(regex_multiple_days, info)
        regex_multiple_weeks2 = re.search(regex_multiple_weeks, info)
        regex_multiple_months2 = re.search(regex_multiple_months, info)
        regex_aday2 = re.search(regex_aday,info)
        regex_meansdaily2 = re.search(regex_meansdaily,info)
        regex_week2 = re.search(regex_week,info)
        regex_month2 = re.search(regex_month, info)
        regex_other_day2 = re.search(regex_other_day, info)
        regex_times2 = re.search(regex_times, info)
        regex_every_month2 = re.search(regex_every_month, info)
        regex_every_week2 = re.search(regex_every_week, info)
        regex_on2 = re.search(regex_on, info)
        regex_weird_weeks2 = re.search(regex_weird_weeks, info)
        regex_hours2 = re.search(regex_hours, info)
        regex_every_day2 = re.search(regex_every_day, info)
        regex_every_day_or2 = re.search(regex_every_day_or, info)
        regex_number_month2 = re.search(regex_number_month, info)
        regex_multiple_year2 = re.search(regex_multiple_year, info)
        regex_52_2 = re.search(regex_52, info)
        regex_12_2 = re.search(regex_12, info)
        regex_7_2 = re.search(regex_7, info)
        if regex_52_2:
        #    print line.strip()
            dose_interval_min = int(convert(regex_52_2.group(1))) * int(7)
            line = txt_id + " " + str(dose_interval_min) 
        elif regex_12_2:
        #    print line.strip()
            dose_interval_min = convert(regex_12_2.group(1))
            line = txt_id + " " + str(dose_interval_min) + " month(s)"
        elif regex_7_2:
            dose_interval_min = convert(regex_7_2.group(1))
            line = txt_id + " " + str(dose_interval_min) 
        elif regex_multiple_days2:
           # print line.strip()
            dose_interval_min = convert(regex_multiple_days2.group(1))
            dose_interval_max = convert(regex_multiple_days2.group(2))    
            line = txt_id + " " + comp(dose_interval_min, dose_interval_max)
        elif regex_every_day_or2:
         #   print line.strip()
            dose_interval_min = convert(regex_every_day_or2.group(1))
            dose_interval_min = convert(regex_every_day_or2.group(2))
            line = txt_id + " " + comp(dose_interval_min, dose_interval_max)
        elif regex_every_day2:
        #    print line.strip()
            dose_interval_min = convert(regex_every_day2.group(1))
            line = txt_id + " " + dose_interval_min
        elif regex_every_week2:
            dose_interval_min = convert(regex_every_week2.group(1))
            dose_in_1 = int(dose_interval_min)*7    
         #   line = txt_id + " " + dose_interval_min+ " week(s)"
            line = txt_id + " " + str(dose_in_1)    
        elif regex_weird_weeks2: ##############################this is for the week - could be 3-7 days or 1 because it is a week, logic dictates 7
          #  print line.strip()     
            line = txt_id + "3-7"       
        elif regex_multiple_weeks2:
          #  print line.strip()
            dose_interval_min = convert(regex_multiple_weeks2.group(1))
            dose_interval_max = convert(regex_multiple_weeks2.group(2))
            dose_in_1 = int(dose_interval_min)*7    
            dose_in_2 = int(dose_interval_max)*7    
            line = txt_id + " " + str(dose_in_1) + "-" + str(dose_in_2) 
        elif regex_every_month2:
          #  print line.strip()
            dose_interval_min = convert(regex_every_month2.group(1))
            line = txt_id + " " + dose_interval_min+ " month(s)"  
        elif regex_number_month2:
           # print line.strip()
            dose_interval_min = convert(regex_number_month2.group(1))
            line = txt_id + " " + dose_interval_min+ " month(s)"              
        elif regex_multiple_months2:
            #print line.strip()
            dose_interval_min = convert(regex_multiple_months2.group(1))
            dose_interval_max = convert(regex_multiple_months2.group(2))    
         #   line = txt_id + " " + dose_interval_min+ "*30" + "-" + dose_interval_max + "*30"   
            line = txt_id + " " + dose_interval_min+ " month(s)" + "-" + dose_interval_max + " month(s)"  
        elif regex_multiple_year2:
            #print line.strip()
            dose_interval_min = convert(regex_multiple_year2.group(1))
            dose_interval_max = convert(regex_multiple_year2.group(2))    
         #   line = txt_id + " " + dose_interval_min+ "*30" + "-" + dose_interval_max + "*30"   
            line = txt_id + " " + dose_interval_min+ " year(s)" + "-" + dose_interval_max + " year(s)"  
        elif regex_other_day2:
            #print line.strip()
            line = txt_id + " " + "2"
        elif "fortnight" in info or "fortnightly" in info:
            #print line.strip()
            line = txt_id + " " + "14"
        elif regex_meansdaily2 or regex_aday2:
        #    print line.strip()
            if regex_month2:
                line = txt_id + " " + "1 month"
            else:
                line = txt_id + " " + "1 "
        elif regex_week2:
#            print line.strip()
            regex_after = re.compile('(?:after)(?:\s+)?([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:weeks|week|wks|wk)')
            regex_after2 = re.search(regex_after, info)
            if regex_after2:
                week_number = convert(regex_after2.group(1))
                week_days = int(week_number)*7
                line = txt_id + " " + "1- " + str(week_days)
            elif "biweekly" in info or "biwkly" in info:
                line = txt_id + " " + "14"
            else:              
                line = txt_id + " " + "7"
        elif regex_month2:
            regex_after = re.compile('(?:after)(?:\s+)?([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:months|month|mth|mnth)')
            regex_after2 = re.search(regex_after, info)
            if regex_after2:
                week_number = convert(regex_after2.group(1))
                line = txt_id + " " + str(week_number) + "month(s)"
            elif "bimonthly" in info:
                line = txt_id + " " + "2 month(s)"
            else:              
                line = txt_id + " " + "1 month"
        elif "hours" in info or "hrs" in info or "hour" in info or "hrly" in info or "hy" in info or "hly" in info:
            if regex_hours2:
                dose_interval = regex_hours2.group(1)
                dose_interval = float(dose_interval)/float(24)
                dose_interval = round(dose_interval, 1)
                if ".0" in str(dose_interval):
                    dose_interval = int(dose_interval)
                    line = txt_id + " " + str(dose_interval)
                else:
                    line = txt_id + " " + str(dose_interval)
            else:
                line = txt_id + " " + "1"
        elif "month" in info:
      #      print line.strip()
            line = txt_id + " " + "1 month"
        elif "week" in info or "wks" in info or "wk" in info or "weeks" in info:
#            print line.strip()
            regex_week_number = re.compile('([0-9])(?:wk)')
            regex_week_number2 = re.search(regex_week_number, info)
            if regex_week_number2:
                di = int(regex_week_number2.group(1))*7
                line = txt_id + " " + str(di)
            else:
            #    print line.strip()
                line = txt_id + " " + "7"
        elif "alternate" in info or "alt" in info: #### here I am assuming that the 1-2 alternate days refers to the dose number. many examples that are extremely ambiguous
            line = txt_id + " " + "2"
        elif regex_on2 or "onprn" in info:
#            print line.strip()
            line = txt_id + " " + "1"
        elif "year" in info:
            if "yearly"==info or "yrly"==info:
                line = txt_id + " " + "12 months"
            else:
                line = txt_id + " " + "12 months"
        elif "min" in info:
          #  print line.strip()
            line = txt_id + " " + "1"
        elif regex_times2 or "day" in info or "hs" in info or "eve" in info or "teatime" in info or "tea time" in info or "dinner time" in info or "lunch time" in info or "night" in info or "midnight" in info or "evening" in info or "hrs" in info or "nightly" in info or "midday" in info or "noon" in info or "afternoon" in info or "dusk" in info or "dawn" in info or "lunchtime" in info or "dinnertime" in info or "noct" in info or "noc" in info:
    #        print line.strip()
            line = txt_id + " " + "1"
        else:
          #  print line.strip()
            line = txt_id + " " + "?"
    new_extracted_dose_interval.write(line+"\n")
new_extracted_dose_interval.close()
