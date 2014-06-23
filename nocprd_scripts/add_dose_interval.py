#!/usr/local/python

# author: george karystianis
# date: 23/01/2013

# this is a script that adds the dose intervals into the columns overall but excludes the cprd columns due to being useless at the end :P

import sys
import re


number_dict={"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "ten":"10", "apply":"1", "applied":"1","half":"0.5", "quarter":"0.25", "a":"1", "once":"1", "tablet":"1"}

def convert(n): #function that converts a word number into a number when it is called :P
    if n in number_dict:
        return number_dict[n]
    else:
        return n

interval_dose_file= open(sys.argv[3], 'w')

frequency_dict = {"once":"1", "twice":"2", "three":"3", "four":"4", "five":"5","six":"6","seven":"7", "eight":"8","nine":"9","ten":"10","eleven":"11","twelve":"12", "bd":"2","b. d":"2","b.d.":"2","b. d.":"2","t.d.s":"3","t.d.s.":"3","t. d. s.":"3", "tds":"3","t.i.d":"3","t.i.d.":"3","t. i. d.":"3", "tid":"3", "tiw":"3", "t.i.w":"3","t.i.w.":"3","t. i. w.":"3","sid":"1","s.i.d":"1","s.i.d.":"1","s. i. d.":"1", "qwk":"1", "q.w.k":"1","q.w.k.":"1","q. w. k.":"1","qqh":"6", "q.q.h" :"6","q.q.h." :"6","q. q. h." :"6","qod":"1", "q.o.d":"1","q.o.d.":"1","q. o. d.":"1", "qid":"4", "q.i.d":"4","q.i.d.":"4","q. i. d.":"4", "qd":"1", "q.d":"1","q.d.":"1","q. d.":"1", "q1d":"1", "q.1.d":"1","q.1.d.":"1","q. 1. d.":"1","am":"1","a.m":"1","a.m.":"1","a. m.":"1", "bis":"2", "b.i.s":"2","b.i.s.":"2","b. i. s.":"2","bid":"2", "b.i.d":"2","b.i.d.":"2","b. i. d.":"2","bt":"1","b.t.":"1","b. t.":"1", "b.t":"1", "hs":"1", "h.s":"1","h.s.":"1","h. s.":"1", "dieb alt":"1","alt":"1","eod":"1","e.o.d":"1","e.o.d.":"1","e. o. d.":"1","mane":"1","on":"1","o.n":"1","o.n.":"1","o. n.":"1","om":"1","o.m":"1","o.m.":"1","o. m.":"1","opd":"1","o.p.d":"1","o.p.d.":"1","o. p. d.":"1","pm":"1","p.m":"1","p.m.":"1","p. m.":"1","two":"2","qad":"1","q.a.d":"1","q.a.d.":"1","q. a. d.":"1",
"qam":"1","q.a.m":"1","q.a.m.":"1","q. a. m.":"1","qds":"4","q.d.s":"4","q.d.s.":"4","q. d. s.":"4","qpm":"1","q.p.m":"1","q.p.m.":"1","q. p. m.":"1","qh":"24","q.h":"24","q.h.":"24","q. h.":"24","qhs":"1","q.h.s":"1","q.h.s.":"1","q. h. s.":"1","q1h":"24", "q.1.h":"24","q.1.h.":"24","q. 1. h.":"24","q2h":"12","q.2.h":"12","q.2.h.":"12","q. 2. h.":"12", "nocte":"1","noct":"1","bds":"2","b.d.s":"2","b.d.s.":"2","b. d. s.":"2", "t.d":"3","t.d.":"3","t. d.":"3", "td":"3", "qh":"24", "q.h":"24","q.h.":"24","q. h.":"24","alt sh":"12",
"q3h":"8","q4h":"6","q5h":"4.8","q6h":"4","q7h":"3.4","q8h":"3","q.3.h":"8","q.4.h":"6","q.5.h":"4.8","q.6.h":"4","q.7.h":"3.4","q.8.h":"3","q.3.h.":"8","q.4.h.":"6","q.5.h.":"4.8","q.6.h.":"4","q.7.h.":"3.4","q.8.h.":"3", "eve":"1", "morning":"1","night": "1", "day":"1", "afternoon":"1", "evening":"1", "one":"1", "midday":"1", "midnight":"1", "teatime":"1", "dusk":"1", "bedtime":"1", "mor":"1", "dawn":"1", "morne":"1",  "morn":"1", "each":"1", "every":"1","twelve":"12", "eleven":"11", "thirteen":"13", "fourteen":"14", "fifteen":"15", "sixteen":"16", "seventeen":"17", "nineteen":"19", "eighteeen":"18", "twenty":"20", "twenty one":"21", "twenty two":"22", "twenty three":"23", "twenty four":"24", "daily":"1", "a month":"1", "tea time":"1", "noon":"1", "nightly":"1", "lunchtime":"1", "lunch time":"1", "bet time":"1", "dinnertime":"1", "dinner time":"1", "other":"2", "twice/":"2", "thrice":"3"}


interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:5}{5:2}{6:5}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format('text_id','|','text', '|', 'DN_min','|','DN_MAX','|','DF_MIN','|','DF_MAX','|','DI_min','|','DI_max','|','required?','|','DU','|','COD')+"\n")  

regex_meansdaily = re.compile('daily|dly|nightly|times\s?a\s?day|^mane$|opd|qam|qds|noc|nocte|^om$|^on$|qpm|qd|q1d|^sid$|qid|tds|qh|q.h|qhs|q1h|q2h|q3h|q4h|q5h|q6h|q7h|q8h|q9hq10h|q11h|q12h|q1|q2|q3|q4|q5|q6|q7|q8|q9|q10|q11|q12|qqh|^am$|pm|bd|tid|q3h|q4h|q5h|q6h|q7h|q8h|q.3.h|q.4.h|every\sday|each\sday|a\sday|o.d.|times/day|\sod|a\snight|a d\say|at\snight|at\sday|q.5.h|q.6.h|q.7.h|q.8.h|q.3.h.|q.4.h.|q.5.h.|q.6.h.|q.7.h.|q.8.h.|noct|o.\sd.|t\sd\ss|in\sthe\smorning|in\sthe\snight|/day|\sday|every\smorning|every\snight|dail|times/d|[0-9]+-od|times/da|[0-9]+\s?od')

regex_every_day = re.compile('(every|each|per)(?:\s+)?(day|night|eve|evening|afternoon|noon|dusk|dawn|midday|midnight|bedtime|teatime|tea\stime|dinnertime|lunchtime|lunch\stime|dinner\stime|noc)')

regex_week = re.compile('(twice)(?:\s+)?(?:a|/)?(?:\s+)?(?:week|wks|wk|weeks)')

regex_once_week = re.compile('(once)(?:\s+)?(?:a|\/)?(?:\s+)?(?:week|wks|wk|weeks)')

regex_long_week = re.compile('(?:once|one)(?:\s+)?(?:a|\/|every|times)?(?:\s+)?(one|two|three|four|five|six|seven|eight|nine|ten|[0-9]+)(?:\s+)?(?:week|wks|wk|weeks)')

regex_once_month = re.compile('(?:once)(?:\s+)?(?:a|\/|every|each)?(?:\s+)?(one|two|three|four|five|six|seven|eight|nine|ten|[0-9]+)(?:\s+)?(?:month|months)')

regex_alt = re.compile('(?:every|each|on|in)?(?:\s+)?(alt|dieb.\salt.|dieb\salt|eod|e.o.d|q.a.d|qad|alt|alternate)(?:\s+)?(day|eve|evening|morne|morning|morn|midnight|night|bedtime|teatime|tea\stime|dinner\stime|dawn|noon|dusk|afternoon|noct|nocte|mane|lunchtime|lunch\stime|dinner\stime|dinnertime|days|noc)')

regex_alt_double = re.compile('(?:every|each|on|in)(?:\s+)?([0-9]|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|to|or)(?:\s+)?([0-9]|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:alt|dieb.\salt.|dieb\salt|eod|e.o.d|q.a.d|qad|alt|alternate)(?:\s+)?(?:day|eve|evening|morne|morning|morn|midnight|night|bedtime|teatime|tea\stime|dinner\stime|dawn|noon|dusk|afternoon|noct|nocte|mane|lunchtime|lunch\stime|dinner\stime|dinnertime|days|noc)')

regex_meal = re.compile('([0-9]|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(after|with|during|before)(?:\s+)?(every|each|per)(?:\s+)?(meal|meals|evening\smeal|lunch|dinner|supper|breakfast|evening\smeals)')

regex_onprn = re.compile('\Aonprn')

regex_onprn_number = re.compile('([0-9])(?:\/)([0-9])(?:onprn)')    

regex_stop = re.compile('(stop\s+for)|([a-z]+\s+break\s)|(day+\s+gap\s)|(discontinue\s+(use|after))')  ### this is for the flaging of breaks - we keep only the dosage unit if extracted and required and choice of dose.




mega={}
mega2={}

interval_flag=0
for line in open(sys.argv[1],'r'): # read the converted_dose_interval_numbers
    if "dose_interval\n"==line:
        interval_flag = 1
        continue
    if interval_flag==1:
        boundary = line.find('pr.')
        boundary2 = line.find('.txt')
        line_id=line[boundary+3:boundary2]
        dose_interval_min = line[boundary2+5:].strip()
        dose_interval_max = dose_interval_min
        regex= re.compile('([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:or|-|to)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)')
        regex2 = re.search(regex, line)
        if regex2:
   #         print line.strip()
            dose_interval_min = str(int(regex2.group(1)))
            dose_interval_max = str(int(regex2.group(2)))
            mega[line_id] = dose_interval_min
            mega2[line_id] = dose_interval_max
        else:
            dose_interval_min = str(dose_interval_min)
            dose_interval_max = str(dose_interval_max)
            mega[line_id] = dose_interval_min
            mega2[line_id] = dose_interval_max
  #      print line_id, dose_interval_min, dose_interval_max

for line in open(sys.argv[2],'r'): # read the file coming from the default file of dose number that contains all the lines that are necessary.
    info = line.split('|')
    line_id2=info[0].strip()
    text_info = info[1].strip().lower()
    dn_min = info[2].strip()
    dn_max = info[3].strip()
    df_min = info[4].strip()
    df_max = info[5].strip()
    required = info[6].strip()
    du = info[7].strip()
    cod = info[8].strip()
    regex_meansdaily2 = re.search(regex_meansdaily, text_info)
    regex_every_day2 = re.search(regex_every_day, text_info)
    regex_week2 = re.search(regex_week, text_info)
    regex_once_week2 = re.search(regex_once_week, text_info)
    regex_long_week2 = re.search(regex_long_week, text_info)
    regex_once_month2 = re.search(regex_once_month, text_info)
    regex_noise = re.compile('[\~]+')
    regex_noise2 = re.search(regex_noise, text_info)
    regex_letter = re.compile('[a-z]+')
    regex_letter2 = re.search(regex_letter, text_info)
    regex_alt2 = re.search(regex_alt, text_info)
    regex_alt_double2 = re.search(regex_alt_double, text_info)
    regex_meal2 = re.search(regex_meal, text_info)#
    regex_onprn2 = re.search(regex_onprn, text_info)
    regex_onprn_number2 = re.search(regex_onprn_number, text_info)
    regex_stop2 = re.search(regex_stop, text_info)
    if 'text_id' in line:
        continue
#    print line.strip()
    if line_id2 not in mega:
    #    print line.strip()
        if regex_onprn2:
            #print line.strip()
         #   interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
            interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', "?",'|',"?",'|',df_min,'|',df_max,'|',"1",'|',"1",'|',required,'|',du,'|',cod)+"\n")   
        elif regex_onprn_number2:  
            dn = float(regex_onprn_number2.group(1))/float(regex_onprn_number2.group(2))
          #  print dn
          #  interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
            interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', str(dn),'|',str(dn),'|',df_min,'|',df_max,'|',"1",'|',"1",'|',required,'|',du,'|',cod)+"\n")
           
        elif regex_noise2:
            if regex_letter2:
            #    interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"1",'|',"?",'|',required,'|',du,'|',cod)+"\n")
            else:
           #     interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"?",'|',"?",'|',required,'|',du,'|',cod)+"\n")
        elif regex_alt_double2:
       #     print line.strip()
            di_min = convert(regex_alt_double2.group(1))
            di_max = convert(regex_alt_double2.group(2))
            di_min = str(int(di_min) + 1)
            di_max = str(int(di_max) + 1)
           # interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
            interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',di_min,'|', di_max,'|',required,'|',du,'|',cod)+"\n")       
        elif regex_alt2:
         #   print line.strip()
          #  interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
            interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"2",'|',"2",'|',required,'|',du,'|',cod)+"\n")   
        elif regex_meal2:
         #   interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
            interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"1",'|',"1",'|',required,'|',du,'|',cod)+"\n")                 
        elif regex_meansdaily2:
          #  interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
            interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"1",'|',"1",'|',required,'|',du,'|',cod)+"\n")

        elif "hrs" in text_info or "hr" in text_info or "hours" in text_info or "hour" in text_info:
         #   interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
            interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"1",'|',"1",'|',required,'|',du,'|',cod)+"\n")

        else:
         #   interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
            interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"1",'|',"?",'|',required,'|',du,'|',cod)+"\n")
    else:
   #     print line.strip()
        if regex_stop2:
            #print text_info ### this is for the break dosages
          #  interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
            interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format("#"+line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|','#','|',"#",'|',required,'|',du,'|',cod)+"\n") 
        elif mega[line_id2]=="?":
            if regex_meansdaily2:
          #      interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")           
                interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"1",'|',"1",'|',required,'|',du,'|',cod)+"\n")
            else:
                if "week"  in text_info or "wks" in text_info or "weekly" in text_info or "wkly" in text_info:
                    if regex_week2:
                #        interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                        interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"3",'|','4','|',required,'|',du,'|',cod)+"\n") 
                    elif regex_once_week2:
                 #       interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                        interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"7",'|','7','|',required,'|',du,'|',cod)+"\n") 
                    elif regex_long_week2:
                        di = convert(regex_long_week2.group(1))
                        di = int(di) * int(7)
                  #      interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                        interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',di,'|',di,'|',required,'|',du,'|',cod)+"\n")
                    else:
                   #     interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                        interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|','7','|','7','|',required,'|',du,'|',cod)+"\n")
                elif "month" in text_info or "mnth" in text_info:
                   # print line.strip()
                    regex_every_month = re.compile('(?:every|each)(?:\s+)?([0-9]+|[a-z]+)(?:\s+)?(?:months|monthly|mthly|month)')
                    regex_every_month2 = re.search(regex_every_month, text_info)
                    if regex_every_month2:
                        di = convert(regex_every_month2.group(1))
                        di = di + " month(s)"
                      #  print di
                   #     interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                        interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',di,'|',di,'|',required,'|',du,'|',cod)+"\n")   
                    else:
                  #      interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                        interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"?",'|',"?",'|',required,'|',du,'|',cod)+"\n")                                     
                else:
                  #  interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                    interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"1",'|',mega2[line_id2],'|',required,'|',du,'|',cod)+"\n")

       # elif regex_alt2:
        #    print line.strip()
         #   interval_dose_file.write#("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
          #  interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',"2",'|',"2",'|',required,'|',du,'|',cod)+"\n")   
      
        else:  
            if regex_alt2:
              #  print line.strip()
                if  mega[line_id2] == "2" and mega2[line_id2]=="2":
                 #   interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                    interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|', "2",'|',"2",'|',required,'|',du,'|',cod)+"\n")   
                else:
                    if mega[line_id2] == "1" and mega2[line_id2]=="1":
                  #      interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                        interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|', "2",'|',"2",'|',required,'|',du,'|',cod)+"\n")   
                    else:
                  #      interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                        interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|', mega[line_id2],'|',mega2[line_id2] ,'|',required,'|',du,'|',cod)+"\n")   
            else:
            #    interval_dose_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
                interval_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:8}{9:2}{10:8}{11:2}{12:8}{13:2}{14:8}{15:2}{16:9}{17:2}{18:10}{19:2}{20:}".format(line_id2,'|',text_info, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',mega[line_id2],'|',mega2[line_id2],'|',required,'|',du,'|',cod)+"\n")        
interval_dose_file.close()  
