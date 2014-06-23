#author: george karystianis

#date: 19/11/2012

#this is a script that scans the original text of the medical prescriptions and extracts the choice of dose - either being o, 1 or 2 maximum

import sys
import re

choice_of_dose_file= open(sys.argv[2], 'w')

choice_of_dose_file.write("{0:7}{1:2}{2:70}{3:3}{4:}".format('text_id',' | ','text', ' | ', 'ECOD')+"\n")  
for line in open(sys.argv[1],'r'):#open the common dosages example file
    info = line.split('\t')
    line_id=info[0]
    text_info = info[1].strip('"').lower()
    choice = info[7].strip()
    regex= re.compile('(take|apply|instil|insert|inject|suck|chew|inhale|spray|use|dissolve|put)\s([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|half|eleven|twelve)\s?(to|or|-)\s?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|half|eleven|twelve)\s?')

    regex2= re.compile('(^([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|half|eleven|twelve)\s?(to|or|[-])\s?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|half|eleven|twelve)\s?)')

    regex3 = re.compile('(one|two|three|four|five|six|seven|eight|nine|ten|[0-9]+|eleven|twelve)\s?(to|-)\s?([0-9]|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s?times')

    regex4 = re.compile('\s(or)\s(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\stimes')

    regex5 = re.compile('(one|two|three|four|five|six|seven|eight|nine|ten|[0-9]+|eleven|twelve)\s?(to|[-])\s?(one|two|three|four|five|six|seven|eight|nine|ten|[0-9]+|eleven|twelve)\s?(hourly|weekly|hrly|wkly|wly|hly)')

    regex6 = re.compile('every\s(one|two|three|four|five|six|seven|eight|nine|ten|[0-9]+|eleven|twelve)\s?(to|[-])\s?(one|two|three|four|five|six|seven|eight|nine|ten|[0-9]+|eleven|twelve)\s(hours|hrs)')

    regex7 = re.compile('[0-9]+\s?(ml|mls|msl)?\s?(or|to|-)\s?[0-9]+\s?(ml|mls|msl)')

    regex8 = re.compile('(qwk|qqh|sid|bis|bos|qad|dieb alt|eod|qh|qus|td|bd|bid|tid|tds|q1h|qhs|tiw|t.i.w|qd|qid|alt h|opd|om|on|nocte|qds|b.d|b.o.s|s.i.d|q.w.k|q.q.h|b.i.s|b.h|q.a.d|e.o.d|q.u.s|q.h|b.i.d|t.i.d|t.d.s|q.1.h|q.d|q.i.d|o.p.d|o.m|o.n|q.d.s|q.2.h|q2h|qod|q.o.d|q.h.s|q.h|qh|hs|h.s|mane|pm|p.m|bt|b.t|am|a.m|q1d|q.1.d|b.d.s|bds)\s?(or|[-])\s?(qwk|qqh|sid|bis|bd|bos|qad|dieb alt|eod|qh|qus|td|bid|tid|tds|q1h|qhs|tiw|t.i.w|qd|qid|alt h|opd|om|on|nocte|qds|b.d|b.o.s|s.i.d|q.w.k|q.q.h|b.i.s|b.h|q.a.d|e.o.d|q.u.s|q.h|b.i.d|t.i.d|t.d.s|q.1.h|q.d|q.i.d|o.p.d|o.m|o.n|q.d.s|q.2.h|q2h|qod|q.o.d|q.h.s|q.h|qh|hs|h.s|mane|pm|p.m|bt|b.t|am|a.m|q1d|q.1.d|b.d.s|bds|q3h|q4h|q5h|q6h|q7h|q8h|q.3.h|q.4.h|q.5.h|q.6.h|q.7.h|q.8.h|q.3.h.|q.4.h.|q.5.h.|q.6.h.|q.7.h.|q.8.h.)')

    regex9 = re.compile('(taken|applied|instilled|inserted|injected|sucked|chewed|inhaled|sprayed|used|dissolved|put)\sor\s(taken|applied|instilled|inserted|injected|sucked|chewed|inhaled|sprayed|used|dissolved|put)')

    regex_upto = re.compile('uptp|up\sto')
    regex = re.search(regex, text_info)
    regex2 = re.search(regex2, text_info)
    regex3 = re.search(regex3, text_info)
    regex4 = re.search(regex4, text_info)
    regex5 = re.search(regex5, text_info)
    regex6 = re.search(regex6, text_info)
    regex7 = re.search(regex7, text_info)
    regex8 = re.search(regex8, text_info)
    regex9 = re.search(regex9, text_info)    
    regex_upto2 = re.search(regex_upto, text_info)   
                                                                                                                         
    if 'textid' in line:
        continue
    if "as required" in text_info or "when required" in text_info or "if required" in text_info or "when needed" in text_info  or "if needed" in text_info or "as needed" in text_info or "pro re nata" in text_info or "sos" in text_info or "sit" in text_info or "siop" in text_info or "si opus sit" in text_info or "p.r.n" in text_info or "as reqd" in text_info or "when reqd" in text_info or "if reqd" in text_info or "as req" in text_info or "when req" in text_info or "if req" in text_info or "prn" in text_info or "p r n" in text_info or "p. r. n" in text_info or "when necessary" in text_info or "if necessary" in text_info or "as necessary" in text_info or "really necessary" in text_info or "absolutely necessary" in text_info:
       # print line.strip()
        mine_choice_of_dose = "2"
        choice_of_dose_file.write("{0:7}{1:2}{2:70}{3:3}{4:4}".format(line_id,' | ',text_info, ' | ', mine_choice_of_dose)+"\n")
    elif regex or regex2 or regex3 or regex4 or regex5 or regex6 or regex7 or regex8 or regex9 or regex_upto2:
      #  print line.strip()
        mine_choice_of_dose = "1"
        choice_of_dose_file.write("{0:7}{1:2}{2:70}{3:3}{4:4}".format(line_id,' | ',text_info, ' | ', mine_choice_of_dose)+"\n")
    else:
        if choice == "0":
            mine_choice_of_dose = "0"
            choice_of_dose_file.write("{0:7}{1:2}{2:70}{3:3}{4:4}".format(line_id,' | ',text_info, ' | ', mine_choice_of_dose)+"\n")
        elif choice == "1":
            mine_choice_of_dose = "?"
            choice_of_dose_file.write("{0:7}{1:2}{2:70}{3:3}{4:4}".format(line_id,' | ',text_info, ' | ', mine_choice_of_dose)+"\n")
        elif choice == "2":
            if "required" in text_info or "needed" in text_info or "necessary" in text_info or "ifreq" in text_info or "asreq" in text_info:
                mine_choice_of_dose = "2"
                choice_of_dose_file.write("{0:7}{1:2}{2:70}{3:3}{4:4}".format(line_id,' | ',text_info, ' | ', mine_choice_of_dose)+"\n")                
            else: ## here I initialize those that had choice of dose 2 when they were simply having 0 - ie three times per day
                mine_choice_of_dose = "0"
                choice_of_dose_file.write("{0:7}{1:2}{2:70}{3:3}{4:4}".format(line_id,' | ',text_info, ' | ', mine_choice_of_dose)+"\n")
               # print line.strip()
choice_of_dose_file.close()  




