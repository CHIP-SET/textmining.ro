#!/usr/local/python

import sys
import re

new_file = open(sys.argv[3],'w')
mega={}
mega2={}
#read the converted dose_frequencies file

regex_nospaces = re.compile('(?:[0-9]+|[0-9]+.[0-9]+)(?:ml|mls|msl|puffs|puff|puf|pufs|tablet|tablets|tabs|tab|capsules|capsule|inh|caps|cap|sachets|sachet|pills|pill|drop|drps|drops|blister|blisters|amps|ampoule|ampoules|amp|sprays|spray|grams|gram|micrograms|microgram|gm|gms|gs|mcgs|mcg|milligrams|milligram|mgs|mg|suppositor|suppository|suppos|ptch|patches|ounces|ounce|lozenge|lozenges|losenge|losenges|millilitres|millilitre|packs|packets|pack|packet|unit|units|pastille|pastilles)(qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am|pm|bid|bt|hs|dieb\salt|eod|mane|on$|om|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct)')

regex_nospaces_onlylatin = re.compile('^(qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am|pm|bid|bt|hs|dieb\salt|eod|mane|on$|om|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct)(?:[a-z])')

regex_nospaces_period = re.compile('(?:[0-9]+|[a-z]+)\sa(day|night)')

frequency_dict = {"once":"1", "twice":"2", "three":"3", "four":"4", "five":"5","six":"6","seven":"7", "eight":"8","nine":"9","ten":"10","eleven":"11","twelve":"12", "bd":"2","b. d":"2","b.d.":"2","b. d.":"2","t.d.s":"3","t.d.s.":"3","t. d. s.":"3", "tds":"3","t.i.d":"3","t.i.d.":"3","t. i. d.":"3", "tid":"3", "tiw":"3", "t.i.w":"3","t.i.w.":"3","t. i. w.":"3","sid":"1","s.i.d":"1","s.i.d.":"1","s. i. d.":"1", "qwk":"1", "q.w.k":"1","q.w.k.":"1","q. w. k.":"1","qqh":"6", "q.q.h" :"6","q.q.h." :"6","q. q. h." :"6","qod":"1", "q.o.d":"1","q.o.d.":"1","q. o. d.":"1", "qid":"4", "q.i.d":"4","q.i.d.":"4","q. i. d.":"4", "qd":"1", "q.d":"1","q.d.":"1","q. d.":"1", "q1d":"1", "q.1.d":"1","q.1.d.":"1","q. 1. d.":"1","am":"1","a.m":"1","a.m.":"1","a. m.":"1", "bis":"2", "b.i.s":"2","b.i.s.":"2","b. i. s.":"2","bid":"2", "b.i.d":"2","b.i.d.":"2","b. i. d.":"2","bt":"1","b.t.":"1","b. t.":"1", "b.t":"1", "hs":"1", "h.s":"1","h.s.":"1","h. s.":"1", "dieb alt":"1","alt":"1","eod":"1","e.o.d":"1","e.o.d.":"1","e. o. d.":"1","mane":"1","on":"1","o.n":"1","o.n.":"1","o. n.":"1","om":"1","o.m":"1","o.m.":"1","o. m.":"1","opd":"1","o.p.d":"1","o.p.d.":"1","o. p. d.":"1","pm":"1","p.m":"1","p.m.":"1","p. m.":"1","two":"2","qad":"1","q.a.d":"1","q.a.d.":"1","q. a. d.":"1",
"qam":"1","q.a.m":"1","q.a.m.":"1","q. a. m.":"1","qds":"4","q.d.s":"4","q.d.s.":"4","q. d. s.":"4","qpm":"1","q.p.m":"1","q.p.m.":"1","q. p. m.":"1","qh":"24","q.h":"24","q.h.":"24","q. h.":"24","qhs":"1","q.h.s":"1","q.h.s.":"1","q. h. s.":"1","q1h":"24", "q.1.h":"24","q.1.h.":"24","q. 1. h.":"24","q2h":"12","q.2.h":"12","q.2.h.":"12","q. 2. h.":"12", "nocte":"1","noct":"1","bds":"2","b.d.s":"2","b.d.s.":"2","b. d. s.":"2", "t.d":"3","t.d.":"3","t. d.":"3", "td":"3", "qh":"24", "q.h":"24","q.h.":"24","q. h.":"24","alt sh":"12",
"q3h":"8","q4h":"6","q5h":"4.8","q6h":"4","q7h":"3.4","q8h":"3","q.3.h":"8","q.4.h":"6","q.5.h":"4.8","q.6.h":"4","q.7.h":"3.4","q.8.h":"3","q.3.h.":"8","q.4.h.":"6","q.5.h.":"4.8","q.6.h.":"4","q.7.h.":"3.4","q.8.h.":"3", "eve":"1", "morning":"1","night": "1", "day":"1", "afternoon":"1", "evening":"1", "one":"1", "midday":"1", "midnight":"1", "teatime":"1", "dusk":"1", "bedtime":"1", "mor":"1", "dawn":"1", "morne":"1",  "morn":"1", "each":"1", "every":"1","twelve":"12", "eleven":"11", "thirteen":"13", "fourteen":"14", "fifteen":"15", "sixteen":"16", "seventeen":"17", "nineteen":"19", "eighteeen":"18", "twenty":"20", "twenty one":"21", "twenty two":"22", "twenty three":"23", "twenty four":"24", "daily":"1", "a month":"1", "tea time":"1", "noon":"1", "nightly":"1", "lunchtime":"1", "lunch time":"1", "bet time":"1", "dinnertime":"1", "dinner time":"1", "other":"2","twice/":"2", "thrice":"3"}

def convert(n): #function that converts a word number into a number when it is called :P
    if n in frequency_dict:
        return frequency_dict[n]
    else:
        return n

frequency_flag=0
for line in open(sys.argv[1],'r'):
 #   print line.strip()
    if "dose_frequency\n"==line:
        frequency_flag = 1
        continue
    if frequency_flag==1:
        if line=="dose1\n":
            continue
        boundary = line.find('pr.')
        boundary2 = line.find('.txt')
        line_id=line[boundary+3:boundary2]
        dose_frequency_min = line[boundary2+5:].strip()
        dose_frequency_max = dose_frequency_min
        regex_multiple= re.compile('([0-9]+/[0-9]+)\s?(?:or|-|to)\s?([0-9]+/[0-9]+)')
        regex= re.compile('([0-9]+)\s?(?:or|-|to)\s?([0-9]+|\?)')
        regex2 = re.search(regex, line)
        regex_multiple2 = re.search(regex_multiple, line)
        if regex_multiple2:
            dose_frequency_min = regex_multiple2.group(1)
            dose_frequency_max = regex_multiple2.group(2)
        elif regex2:
            if regex2.group(2)=="?":
                dose_frequency_min = str(int(regex2.group(1)))
                dose_frequency_max = "?"
            else:
               dose_frequency_min = str(int(regex2.group(1)))
               dose_frequency_max = str(int(regex2.group(2)))
        dose_frequency_min = str(dose_frequency_min)
        dose_frequency_max = str(dose_frequency_max)
        mega[line_id] = dose_frequency_min
        mega2[line_id] = dose_frequency_max


new_file.write("{0:7}{1:2}{2:70}{3:2}{4:7}{5:2}{6:}".format('text_id','|','text', '|','DF_min','|','DF_max')+"\n")

for line in open(sys.argv[2],'r'):
  #  print line.strip()
    info = line.split('\t')
    # i can get the elements from here. now i am focusing on the second column
    dose_frequency2=info[5]
    line_id2=info[0]
    text_info = info[1].strip('"')
    if 'textid' in line:
        continue
    if line_id2 not in mega:
        new_file.write("{0:7}{1:2}{2:70}{3:2}{4:7}{5:2}{6:}".format(line_id2,'|',text_info, '|', '?','|','?')+"\n")
    else: ## this is hacking for the dose frequency of the spans that have no spaces between them and mentioning of latin phrases for frequency
        text_info2 = text_info.lower()
        regex_nospaces2 = re.search(regex_nospaces,text_info2)
        regex_nospaces_onlylatin2 = re.search(regex_nospaces_onlylatin, text_info2)
        regex_nospaces_period2 = re.search(regex_nospaces_period, text_info2)
        if regex_nospaces2:
            actual_dose_frequency = convert(regex_nospaces2.group(1))
            new_file.write("{0:7}{1:2}{2:70}{3:2}{4:7}{5:2}{6:}".format(line_id2,'|',text_info, '|', actual_dose_frequency,'|',actual_dose_frequency)+"\n")
        elif regex_nospaces_onlylatin2:
            actual_dose_frequency = convert(regex_nospaces_onlylatin2.group(1))
            new_file.write("{0:7}{1:2}{2:70}{3:2}{4:7}{5:2}{6:}".format(line_id2,'|',text_info, '|', actual_dose_frequency,'|',actual_dose_frequency)+"\n")
        elif regex_nospaces_period2:
            actual_dose_frequency = convert(regex_nospaces_period2.group(1))
            new_file.write("{0:7}{1:2}{2:70}{3:2}{4:7}{5:2}{6:}".format(line_id2,'|',text_info, '|', actual_dose_frequency,'|',actual_dose_frequency)+"\n")
        else:                
            new_file.write("{0:7}{1:2}{2:70}{3:2}{4:7}{5:2}{6:}".format(line_id2,'|',text_info, '|', mega[line_id2],'|',mega2[line_id2])+"\n")                   
new_file.close()
