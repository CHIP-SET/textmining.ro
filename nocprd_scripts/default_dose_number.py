#!/usr/local/python

#this is a script that defaults the dose number into 1 if there is an extracted dose frequency, if not then if there is a verb mention into the prescription i.e., taken, add etc. Additionally, if we do not know the dose number and the dose frequency these two have been replaced with ?. 

#author:george karystianis

#date: 22/01/2013

import sys
import re

frequency_dose_file= open(sys.argv[2], 'w')
frequency_dose_file2= open(sys.argv[3], 'w')


number_dict={"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "ten":"10", "eleven":"11", "twelve":"12"}

def convert(n): #function that converts a word number into a number when it is called :P
    if n in number_dict:
        return number_dict[n]
    else:
        return n

def hour_strip(n):
    x = float(24)/float(n)
    if ".0" in str(x):
        x = str(int(x))
    else:
        x=str(round(x,1))
    return x

def no_zero(n):
    if ".0" in str(n):
        n = str(int(n))
    else:
        n = str(round(n,1))
    return n

def no_zero(n):
    if ".0" in str(n):
        n = str(int(n))
    else:
        n = str(round(n,1))
    return n

def double_dose(x, y):
    dose_number_1 = float(convert(x))
    dose_number_2 = float(convert(y))
    actual_dose = (dose_number_1+dose_number_2)/2
    actual_dose = no_zero(actual_dose)
    return actual_dose


number_dict = {"once":"1", "twice":"2", "three":"3", "four":"4", "five":"5","six":"6","seven":"7", "eight":"8","nine":"9","ten":"10","eleven":"11","twelve":"12", "bd":"2","b. d":"2","b.d.":"2","b. d.":"2","t.d.s":"3","t.d.s.":"3","t. d. s.":"3", "tds":"3","t.i.d":"3","t.i.d.":"3","t. i. d.":"3", "tid":"3", "tiw":"3", "t.i.w":"3","t.i.w.":"3","t. i. w.":"3","sid":"1","s.i.d":"1","s.i.d.":"1","s. i. d.":"1", "qwk":"1", "q.w.k":"1","q.w.k.":"1","q. w. k.":"1","qqh":"6", "q.q.h" :"6","q.q.h." :"6","q. q. h." :"6","qod":"1", "q.o.d":"1","q.o.d.":"1","q. o. d.":"1", "qid":"4", "q.i.d":"4","q.i.d.":"4","q. i. d.":"4", "qd":"1", "q.d":"1","q.d.":"1","q. d.":"1", "q1d":"1", "q.1.d":"1","q.1.d.":"1","q. 1. d.":"1","am":"1","a.m":"1","a.m.":"1","a. m.":"1", "bis":"2", "b.i.s":"2","b.i.s.":"2","b. i. s.":"2","bid":"2", "b.i.d":"2","b.i.d.":"2","b. i. d.":"2","bt":"1","b.t.":"1","b. t.":"1", "b.t":"1", "hs":"1", "h.s":"1","h.s.":"1","h. s.":"1", "dieb alt":"1","alt":"1","eod":"1","e.o.d":"1","e.o.d.":"1","e. o. d.":"1","mane":"1","on":"1","o.n":"1","o.n.":"1","o. n.":"1","om":"1","o.m":"1","o.m.":"1","o. m.":"1","opd":"1","o.p.d":"1","o.p.d.":"1","o. p. d.":"1","pm":"1","p.m":"1","p.m.":"1","p. m.":"1","two":"2","qad":"1","q.a.d":"1","q.a.d.":"1","q. a. d.":"1",
"qam":"1","q.a.m":"1","q.a.m.":"1","q. a. m.":"1","qds":"4","q.d.s":"4","q.d.s.":"4","q. d. s.":"4","qpm":"1","q.p.m":"1","q.p.m.":"1","q. p. m.":"1","qh":"24","q.h":"24","q.h.":"24","q. h.":"24","qhs":"1","q.h.s":"1","q.h.s.":"1","q. h. s.":"1","q1h":"24", "q.1.h":"24","q.1.h.":"24","q. 1. h.":"24","q2h":"12","q.2.h":"12","q.2.h.":"12","q. 2. h.":"12", "nocte":"1","noct":"1","bds":"2","b.d.s":"2","b.d.s.":"2","b. d. s.":"2", "t.d":"3","t.d.":"3","t. d.":"3", "td":"3", "qh":"24", "q.h":"24","q.h.":"24","q. h.":"24","alt sh":"12",
"q3h":"8","q4h":"6","q5h":"4.8","q6h":"4","q7h":"3.4","q8h":"3","q.3.h":"8","q.4.h":"6","q.5.h":"4.8","q.6.h":"4","q.7.h":"3.4","q.8.h":"3","q.3.h.":"8","q.4.h.":"6","q.5.h.":"4.8","q.6.h.":"4","q.7.h.":"3.4","q.8.h.":"3", "eve":"1", "morning":"1","night": "1", "day":"1", "afternoon":"1", "evening":"1", "one":"1", "midday":"1", "midnight":"1", "teatime":"1", "dusk":"1", "bedtime":"1", "mor":"1", "dawn":"1", "morne":"1",  "morn":"1", "each":"1", "every":"1","twelve":"12", "eleven":"11", "thirteen":"13", "fourteen":"14", "fifteen":"15", "sixteen":"16", "seventeen":"17", "nineteen":"19", "eighteeen":"18", "twenty":"20", "twenty one":"21", "twenty two":"22", "twenty three":"23", "twenty four":"24", "daily":"1", "a month":"1", "tea time":"1", "noon":"1", "nightly":"1", "lunchtime":"1", "lunch time":"1", "bet time":"1", "dinnertime":"1", "dinner time":"1", "other":"2", "every day":"1", "every night":"1", "a":"1", "thrice":"3"}

regex_latin = re.compile('qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am\Z|pm|bid|bt|hs|dieb\salt|eod|mane|\Aonprn|on\Z|om\Z|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct|b.\sd|q3h|q4h|q5h|q6h|q7h|q8h|alt')

regex_times = re.compile('([a-z]+)(?:\s+)?(?:times|a\sday|a\snight|at\snight|daily|every\sday|every\snight|on\Z)')

frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:5}{5:2}{6:5}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format('text_id','|','text', '|', 'DN_min','|','DN_MAX','|','DF_MIN','|','DF_MX','|','required?','|','DU','|','COD')+"\n")  

regex_oml = re.compile('(?:oml|omls)(?:\s+)?(every\sday|at\snight|every\snight|daily|on\Z)')

regex_every = re.compile('(every\sday|at\snight|every\snight|daily|on\Z)')

regex_problematic_times = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:times|time)(?:\s+)?(?:a|per|an|the|/)?(?:\s)?(?:[a-z]+)')

regex_problematic_times_double = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|to|or)?(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:times|time)(?:\s+)?(?:a\s?day|daily|nightly|monthly|yearly|week|wk|night)')##

regex_problematic_doses_double = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|to|or)?(?:\s+)?([0-9]+|[0-9].[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:times|time)(?:\s+)?(?:a\sday|daily|\/day)')##

regex_double_meal_complicated = re.compile('(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|twenty|[0-9])(?:\s+)?(?:times|time)(?:\s+)?(?:each|every|a|an|in|at|per|during|after|before|with)(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)(?:\s+)?(?:[a-z]+)(?:\s+)?(?:main\smeal|meal|dinner|breakfast|lunch|supper|food|evening\smeal)(?:\s+)?(?:and)?(?:\s+)?(?:[0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:each|every|a|an|in|at|per|during|after|before|with)(?:\s+)?(morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)')


regex_problematic_doses_and_freqs = re.compile('([0-9]+|[0-9].[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|to|or)?(?:\s+)?([0-9]+|[0-9].[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|to|or)?(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:times|time)(?:\s+)?(?:a\s?day|daily)')


regex_problematic_doses_triple = re.compile('([0-9]+|[0-9].[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)([0-9]+|[0-9].[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)(?:-|to|or)?(?:\s+)([0-9]+|[0-9].[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:times|time)(?:\s+)?(?:a\s?day|daily)')

regex_apply_du_double = re.compile('(?:apply)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|to|or)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|pastille|pastilles|drops|drop|drps|drp|drs|dr|ampoule|ampoules|unit|units|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|mcg|mg|mgs|g\Z|gs|ml|msl|millilitre|millilitres|pack|packet|packs|packets)')

regex_apply_du_single = re.compile('(?:apply)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|pastille|pastilles|drops|drop|unit|units|drps|drp|drs|dr|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|mcg|mg|mgs|g\Z|gs|ml|msl|millilitre|millilitres|pack|packet|packs|packets)')

regex_every_week = re.compile('(every|each)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(week|weeks|wks|wk)')

regex_double_dose = re.compile('([0-9]+)\s([0-9]+)')

regex_double_dose_word = re.compile('([0-9]+)(?:\s+)([0-9]+)(?:\s+)?(apply|chew|take|insert|use|instil|inject|suck|spray|inhale|dissolve|put)?(?:\s+)?(?:every|each|at|during|after|before|a|an)?(?:\s+)?(morning|evening|afternoon|night|midnight|midday|day|mor|dusk|bedtime|eve|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed|noc)')

regex_dose_hr = re.compile('([0-9]+)(?:\s+)(?:[0-9]+)(?:\s+)?(?:hr|hrs)')

regex_freq_hr = re.compile('(?:[0-9]+)(?:\s+)([0-9]+)(?:\s+)?(?:hr|hrs)')

regex_difficult_times = re.compile('([0-9]+)(?:\s+)?(om|on|pm|am)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+\/[0-9]+)(?:\s+)?(on\Z|om\Z|pm|am)')

regex_super_difficult_times = re.compile('([0-9]+)(?:\s+)?(?:times|time)(?:\s+)?(?:a|per|the|/)(?:\s+)?(?:[a-z]+)(?:\s+)?(?:and)?(?:\s+)?(?:[0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:[a-z]+)(?:\s+)([a-z]+)')

regex_super_difficult_times_double = re.compile('([0-9]+)(?:\s+)?(?:-|or|to)(?:\s+)?([0-9]+)(?:\s+)?(?:times|time)(?:\s+)?(?:a|per|the|/)(?:\s+)?(?:[a-z]+)(?:\s+)?(?:and)?(?:\s+)?(?:[0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:[a-z]+)(?:\s+)([a-z]+)')

regex_super_difficult_doses = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:[0-9]+)(?:\s+)?(?:times|time)(?:\s+)?(?:a|per|the|/)(?:\s+)?(?:[a-z]+)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:[a-z]+)(?:\s+)([a-z]+)')

regex_no_dose_verb = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)(?:take|use|insert|chew|suck|instill|spray|apply|inhale|dissolve|inject|put)(?:\s+)(?:every|each)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|or|to)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)(?:times|time|days|day|weeks|wks|week)')

regex_no_dose = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)(days|day|weeks|wks|week|month|months|hours|hrs|nights|years|year|yrs)')

regex_hour_stuff = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|or|to)?(?:\s+)?(?:[0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)?(?:\s+)?(?:hrly|hry|hly)')

regex_every_days = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)(every|each)(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(\/)?(?:\s+)?(days|day|month|months|weeks|wks|week|wk|years|year|yrs|nights|night|52|12)(?:\s+)(?:\|)')

regex_alt_days = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:\/)?(?:\s+)?(?:[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(alt.|alt|alternate|dieb\salt)(?:\s+)?(days|day|month|months|weeks|wks|week|wk|years|year|yrs|nights|night|52|12)(?:\s+)(?:\|)')

regex_timeunit = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)(daily|dly|nightly|wkly|weekley|monthly|mthly|mnthly|yearly|yrly|weekly|wkly|biweekly|bimonthly)(?:\s+)(?:\|)')


regex_times_no_dose = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|or|to)?(?:\s+)?(?:[0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)?(?:\s+)?(?:times|time)(?:\s+)?(a\s+day|daily|nightly|per\s+day)')

regex_difficult_dose_number = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am|pm|bid|bt|hs|dieb\salt|eod|mane|on\Z|om|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct)(?:\s+)?([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am|pm|bid|bt|hs|dieb\salt|eod|mane|on\Z|om|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct)')

regex_max_times = re.compile('(?:maximum|max)(?:\s+)([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)(?:times)')

for line in open(sys.argv[1],'r'):
    if "text_id" in line:
        continue
    info = line.split('|')
    text = info[0].strip()
    information = info[1].strip().lower()
    dn_min = info[2].strip()
    dn_max = info[3].strip()
    df_min = info[4].strip()
    df_max = info[5].strip()
    required = info[6].strip()
    du = info[7].strip()
    cod = info[8].strip()
    regex_hours = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|to|or)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|nineteen|twenty)(?:\s+)?(?:hours|hrs|hourly|hrly|hly|hy|hour)')
    regex_word_hourly = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:hours|hrs|hourly|hrly|hly|hour|hr|hy)')
    regex_times2 = re.search(regex_times, information)
    regex_hours2 = re.search(regex_hours, information)
    regex_word_hourly2 = re.search(regex_word_hourly,information)
    regex_latin2 = re.search(regex_latin, information)
    regex_oml2 = re.search(regex_oml, information)
    regex_every2 = re.search(regex_every, information)
    regex_problematic_times2 = re.search(regex_problematic_times, information)
    regex_problematic_times_double2 = re.search(regex_problematic_times_double, information)
    regex_apply_du_double2 = re.search(regex_apply_du_double,information)
    regex_apply_du_single2 = re.search(regex_apply_du_single, information)
    regex_every_week2 = re.search(regex_every_week, information)
    regex_double_dose_dn_min = re.search(regex_double_dose, dn_min)
    regex_double_dose_dn_max = re.search(regex_double_dose, dn_max)
    regex_dose_hr2 = re.search(regex_dose_hr, information)
    regex_difficult_times2 = re.search(regex_difficult_times, information)
    regex_super_difficult_times2 = re.search(regex_super_difficult_times, information)
    regex_super_difficult_doses2 = re.search(regex_super_difficult_doses, information)
    regex_problematic_doses_double2 = re.search(regex_problematic_doses_double, information)
    regex_problematic_doses_triple2 = re.search(regex_problematic_doses_triple, information) 
    regex_freq_hr2 = re.search(regex_freq_hr, information)
    regex_double_dose_word2 = re.search(regex_double_dose_word, information)
    regex_problematic_doses_and_freqs2 = re.search(regex_problematic_doses_and_freqs, information)
    regex_no_dose_verb2= re.search(regex_no_dose_verb, line.strip())
    regex_no_dose2= re.search(regex_no_dose, line.strip())
    regex_hour_stuff2 = re.search(regex_hour_stuff, line.strip())
    regex_double_meal_complicated2 = re.search(regex_double_meal_complicated, information)
    regex_every_days2 = re.search(regex_every_days, line.strip())
    regex_alt_days2 = re.search(regex_alt_days, line.strip())
    regex_timeunit2 = re.search(regex_timeunit, line.strip())
    regex_super_difficult_times_double2 = re.search(regex_super_difficult_times_double , information)
    regex_times_no_dose2 = re.search(regex_times_no_dose, information )
    regex_difficult_dose_number2 = re.search(regex_difficult_dose_number, information)
    regex_max_times2 = re.search(regex_max_times, information) 

    if df_min=="yearly" or df_min=="yrly":
        if required=="yes":
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"0",'|',"1",'|',required,'|',du,'|',cod)+"\n")        
        else:
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"1",'|',"1",'|',required,'|',du,'|',cod)+"\n")
    
    elif df_min=="hrly" or df_min=="hourly" or df_min=="hly" or df_min=="hy" or df_max=="hourly" or df_max=="hly" or df_max=="hrly" or df_max=="hy" or df_max=="hrlyprn" or df_min == "hrlyprn" :
        if regex_hours2 and required =="yes":
            hour_1 = float(convert(regex_hours2.group(1)))
            actual_dose_frequency_max = hour_strip(hour_1)
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"0",'|',actual_dose_frequency_max,'|',required,'|',du,'|',cod)+"\n")

        elif regex_hours2 and required =="no":
        #    print line.strip()
            hour_1 = float(convert(regex_hours2.group(1)))
            hour_2 = float(convert(regex_hours2.group(2)))
            actual_dose_frequency_min = hour_strip(hour_2)
            actual_dose_frequency_max = hour_strip(hour_1)
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',actual_dose_frequency_min,'|',actual_dose_frequency_max,'|',required,'|',du,'|',cod)+"\n")       
                   
        elif regex_word_hourly2 and required =="no":
         #   print line.strip()
            hour_1 = float(convert(regex_word_hourly2.group(1)))
            actual_dose_frequency = hour_strip(hour_1)
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',actual_dose_frequency,'|',actual_dose_frequency,'|',required,'|',du,'|',cod)+"\n") 

        elif regex_word_hourly2 and required =="yes":
           # print line.strip()
            hour_1 = float(convert(regex_word_hourly2.group(1)))
            actual_dose_frequency = hour_strip(hour_1)
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|','0','|',actual_dose_frequency,'|',required,'|',du,'|',cod)+"\n") 

        else:
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"24",'|',"24",'|',required,'|',du,'|',cod)+"\n") 

    elif regex_problematic_doses_and_freqs2:
      #  print line.strip()
        if required == "yes":
            dn_min = convert(regex_problematic_doses_and_freqs2.group(1))
            dn_max = convert(regex_problematic_doses_and_freqs2.group(2))
            df = convert(regex_problematic_doses_and_freqs2.group(4))
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"0",'|',df,'|',required,'|',du,'|',cod)+"\n") 
        else:
            dn_min = convert(regex_problematic_doses_and_freqs2.group(1))
            dn_max = convert(regex_problematic_doses_and_freqs2.group(2))
            df_min = convert(regex_problematic_doses_and_freqs2.group(3))
            df_max = convert(regex_problematic_doses_and_freqs2.group(4))
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n") 

    elif regex_problematic_doses_triple2:
    #    print line.strip()
        dn_min = convert(regex_problematic_doses_triple2.group(1))
        dn_max = convert(regex_problematic_doses_triple2.group(3))
        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n") 

    elif regex_problematic_doses_double2:
      #  print line.strip()
        if regex_double_meal_complicated2:
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n") 
        else:
            if required == "yes":
                dn_min = convert(regex_problematic_doses_double2.group(1))
                dn_max = convert(regex_problematic_doses_double2.group(2))
                df = convert(regex_problematic_doses_double2.group(3))
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"0",'|',df,'|',required,'|',du,'|',cod)+"\n") 
            else:
                dn_min = convert(regex_problematic_doses_double2.group(1))
                dn_max = convert(regex_problematic_doses_double2.group(2))
                df = convert(regex_problematic_doses_double2.group(3))
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df,'|',df,'|',required,'|',du,'|',cod)+"\n") 


    elif regex_problematic_times_double2:
    #    print line.strip()
        if required=="yes":
            df_max = convert(regex_problematic_times_double2.group(2))
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n") 
        else:
            df_min = convert(regex_problematic_times_double2.group(1))
            df_max = convert(regex_problematic_times_double2.group(2))
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")

    elif regex_problematic_times2:
      #  print line.strip()
        new_dn = convert(regex_problematic_times2.group(1))
        if "max" in information or "up to" in information or "upto" in information:
            df_max = convert(regex_problematic_times2.group(2))
            if required=="yes":
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|',new_dn,'|',"0",'|',df_max,'|',required,'|',du,'|',cod)+"\n") 
            else:
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|',new_dn,'|',df_max,'|',df_max,'|',required,'|',du,'|',cod)+"\n") 
        elif required=="yes":
            df_max = convert(regex_problematic_times2.group(2))
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', new_dn,'|',new_dn,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n") 
        else:
            df_max = convert(regex_problematic_times2.group(2))
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', new_dn,'|',new_dn,'|',df_max,'|',df_max,'|',required,'|',du,'|',cod)+"\n")
   
    elif regex_apply_du_single2:
    #    print line.strip()
        if regex_apply_du_double2:
            dn_min = convert(regex_apply_du_double2.group(1))
            dn_max = convert(regex_apply_du_double2.group(2))
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_max,'|',df_max,'|',required,'|',du,'|',cod)+"\n")           
        else:
            dn_min = convert(regex_apply_du_single2.group(1))
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_min,'|',df_max,'|',df_max,'|',required,'|',du,'|',cod)+"\n") 

    elif regex_every_week2:
   #     print line.strip()
        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "?",'|',"?",'|',df_max,'|',df_max,'|',required,'|',du,'|',cod)+"\n")         

    elif regex_double_dose_dn_min and regex_double_dose_dn_max:
  #      print line.strip()
        if regex_dose_hr2:
            dn = regex_dose_hr2.group(1)
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|',dn,'|',dn,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n") 
        else:
            dose_number_min = regex_double_dose_dn_min.group(1)
            dose_number_max = regex_double_dose_dn_max.group(2)
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|',dose_number_min,'|',dose_number_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n") 


    elif regex_difficult_times2:
      #  print line.strip()
        if required =="yes":
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"0",'|', "2",'|',required,'|',du,'|',cod)+"\n") 
        else:
            if "hour" in information:
               # print line.strip()
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n") 
            else:
         #       print line.strip()
                regex_only_om = re.compile('([0-9]|[0-9]\/[0-9]|[0-9].[0-9])(?:\s+)?(?:om|on|am|pm)(?:\s+)?(?:and)?(?:\s+)?([0-9]|[0-9]\/[0-9]|[0-9].[0-9])(?:\s+)?(?:om|on|am|pm)')
                regex = re.search(regex_only_om,information)
                regex_number = re.compile('([0-9])(?:\/)([0-9])')
                if "take one" in information:
                    frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"2",'|', "2",'|',required,'|',du,'|',cod)+"\n") 
                elif regex:
                    dn_1 = regex.group(1)
                    dn_2 = regex.group(2)
                    if "/" in dn_1:
                        regex_number2 = re.search(regex_number, dn_1)
                        dn_1 = float(regex_number2.group(1))/float(regex_number2.group(2))
                    if "/" in dn_2:
                        regex_number2 = re.search(regex_number,dn_2)
                        dn_2 = float(regex_number2.group(1))/float(regex_number2.group(2))
                    dn = (float(dn_1) + float(dn_2))/2
                    dn = no_zero(dn)
                    frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn,'|',dn,'|',"2",'|', "2",'|',required,'|',du,'|',cod)+"\n") 
                else:
                    frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"2",'|', "2",'|',required,'|',du,'|',cod)+"\n") 

    elif regex_super_difficult_times_double2:
   #     print line.strip()
        if required =="yes":
            df_min = regex_super_difficult_times_double2.group(1)
            df_max = convert(regex_super_difficult_times_double2.group(2))
            if regex_super_difficult_doses2:
                dn = double_dose(regex_super_difficult_doses2.group(1),regex_super_difficult_doses2.group(2))
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn,'|',dn,'|',"0",'|', df_max,'|',required,'|',du,'|',cod)+"\n")
            else:  
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"0",'|', df_max,'|',required,'|',du,'|',cod)+"\n") 
        else:
         #   print line.strip()
            df_min = regex_super_difficult_times_double2.group(1)
            df_max = convert(regex_super_difficult_times_double2.group(2))
            if regex_super_difficult_doses2:
                dn = double_dose(regex_super_difficult_doses2.group(1),regex_super_difficult_doses2.group(2))
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn,'|',dn,'|',df_min,'|', df_max,'|',required,'|',du,'|',cod)+"\n")
            else:  
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_min,'|', df_min,'|',required,'|',du,'|',cod)+"\n") 

    elif regex_super_difficult_times2:
   #     print line.strip()
        if required =="yes":
            df_min = regex_super_difficult_times2.group(1)
            df_max = convert(regex_super_difficult_times2.group(2))
            df = str(int(df_min) + int(df_max))
            if regex_super_difficult_doses2:
                dn = double_dose(regex_super_difficult_doses2.group(1),regex_super_difficult_doses2.group(2))
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn,'|',dn,'|',"0",'|', df,'|',required,'|',du,'|',cod)+"\n")
            else:  
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"0",'|', df,'|',required,'|',du,'|',cod)+"\n") 
        else:
         #   print line.strip()
            df_min = regex_super_difficult_times2.group(1)
            df_max = convert(regex_super_difficult_times2.group(2))
            df = str(int(df_min) + int(df_max))
            if regex_super_difficult_doses2:
                dn = double_dose(regex_super_difficult_doses2.group(1),regex_super_difficult_doses2.group(2))
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn,'|',dn,'|',df,'|', df,'|',required,'|',du,'|',cod)+"\n")
            else:  
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df,'|', df,'|',required,'|',du,'|',cod)+"\n") 

    elif regex_double_dose_word2:
        #print line.strip()
        dn_min = regex_double_dose_word2.group(1)
        dn_max = regex_double_dose_word2.group(2)
        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_min,'|', df_max,'|',required,'|',du,'|',cod)+"\n") 

    elif regex_no_dose_verb2: #### check out this one the frequencies - changed from df-min and df_max having ? now they show the original extracted df that was correct in the first place.
      #  print line.strip()
        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|', "1",'|',df_min,"|",df_max,'|',required,'|',du,'|',cod)+"\n") 

    elif regex_no_dose2:
        #print line.strip()
        number=	regex_no_dose2.group(1)
        variable = regex_no_dose2.group(2)
        if variable == "hours" or variable == "hrs":
            if required == "yes":
                df_max = float(convert(number))
                df_max = float(24)/df_max
                df_max = no_zero(df_max)
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "?",'|', "?",'|',"0",'|', df_max,'|',required,'|',du,'|',cod)+"\n")
            else:
                df_max = float(convert(number))
                df_max = float(24)/df_max
                df_max = no_zero(df_max)
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "?",'|', "?",'|',df_max,'|', df_max,'|',required,'|',du,'|',cod)+"\n")
        else:
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "?",'|', "?",'|',df_min,'|', df_max,'|',required,'|',du,'|',cod)+"\n")

    elif regex_every_days2 or regex_alt_days2 or regex_timeunit2:
      #  print line.strip()
        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "?",'|', "?",'|',"?",'|', "?",'|',required,'|',du,'|',cod)+"\n")

    elif regex_hour_stuff2:
    #    print line.strip()
        single_dose_single_fre = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:x|\*|\/)?(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:hrly|hly)')
        single_dose_single_fre2 = re.search(single_dose_single_fre, line.strip())
        single_dose_double_fre = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:\*|-)?([0-9]+)(?:\s+)?(?:-|to|or|\/)?(?:\s+)?([0-9]+)(?:\s+)?(?:hrly|hly)')
        single_dose_double_fre2 = re.search(single_dose_double_fre, line.strip())
        double_dose_single_fre = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|to|or)?(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-)?([0-9]+)(?:\s+)?(?:hrly|hly)')
        double_dose_single_fre2 = re.search(double_dose_single_fre, line.strip())
        double_dose_double_fre = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|to|or)?(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)([0-9]+)(?:\s+)?(?:-|to|or)?(?:\s+)?([0-9]+)(?:\s+)?(?:hrly|hly)')
        double_dose_double_fre2 = re.search(double_dose_double_fre, line.strip())
        single_fre = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)([0-9]+)(?:\s+)?(?:hrly|hly)')
        single_fre2 = re.search(single_fre, line.strip())
        double_fre = re.compile('(?:[0-9]+)(?:\s+)(?:\|)(?:\s+)([0-9]+)(?:\s+)?(?:-|to|or)(?:\s+)?([0-9]+)(?:\s+)?(?:hrly|hly)')
        double_fre2 = re.search(double_fre, line.strip())
        if single_dose_single_fre2:
         #   print line.strip()
            dn = single_dose_single_fre2.group(1)
            df = single_dose_single_fre2.group(2)
            if required =="yes":
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn,'|',dn,'|','0','|',df,'|',required,'|',du,'|',cod)+"\n")
            else:
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn,'|',dn,'|',df,'|',df,'|',required,'|',du,'|',cod)+"\n")
        elif single_dose_double_fre2:
          #  print line.strip()
            dn = str(convert(single_dose_double_fre2.group(1)))
            df_min = str(int(24)/int(single_dose_double_fre2.group(3)))
            df_max = str(int(24)/int(single_dose_double_fre2.group(2)))
            if required =="yes":
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn,'|', dn,'|','0','|',df_max,'|',required,'|',du,'|',cod)+"\n")
            else:
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn,'|', dn,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")
        elif double_dose_single_fre2 or double_dose_double_fre2:
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|', dn_min,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")
        elif single_fre2:
          #  print line.strip()
            if required =="yes":
                df_max = float(24)/float(single_fre2.group(1))
                df_max = no_zero(df_max)
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|', "1",'|',"0",'|',df_max,'|',required,'|',du,'|',cod)+"\n")
            else:
                df = float(24)/float(single_fre2.group(1))
                df = no_zero(df)
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|', "1",'|',df,'|',df,'|',required,'|',du,'|',cod)+"\n")

        elif double_fre2:
    #        print line.strip()
            if required =="yes":
                df_max = float(24)/float(double_fre2.group(2))
                df_max=no_zero(df_max)
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|', "1",'|',"0",'|',df_max,'|',required,'|',du,'|',cod)+"\n")
            else:
       #         print line.strip()
                df_max = float(24)/float(double_fre2.group(1))
                df_min = float(24)/float(double_fre2.group(2))
                df_max = no_zero(df_max)
                df_min = no_zero(df_min)                
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|', "1",'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")
        else:
#            print line.strip()
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|', dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")

    elif regex_difficult_dose_number2:
       # print line.strip()
        regex_am = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:@)?(?:\s+)?(?:am|om|pm|[0-9]+am|[0-9]+pm|[0-9]+\s+am|[0-9]+\s+pm)(?:\s+)?([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:@)?(?:\s+)?(am|pm|om|nocte|[0-9]+am|[0-9]+pm|[0-9]+\s+am|[0-9]+\s+pm)')
        regex = re.compile('cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|drops|pastille|pastilles|drop|unit|units|drps|drp|drs|dr|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|mcg|mg|mgs|g\Z|gs|ml|msl|millilitre|millilitres|pack|packet|packs|packets')
        regex_am2= re.search(regex_am, information)
        if regex_am2:
            if re.search(regex, information):
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|',dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")
            else:             
                dn = (float(convert(regex_am2.group(1))) + float(convert(regex_am2.group(2))))/float(2)
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|',dn,'|',dn,'|',"2",'|',"2",'|',required,'|',du,'|',cod)+"\n")            
        else:
         #   print line.strip()
            total_dn = (float(convert(regex_difficult_dose_number2.group(1))) + float(convert(regex_difficult_dose_number2.group(2))))/float(2)
            total_dn = no_zero(total_dn)
            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn,'|', dn,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")    

    elif regex_max_times2:
        df_max = convert(regex_max_times2.group(1))
        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|', dn_max,'|',"1",'|',df_max,'|',required,'|',du,'|',cod)+"\n") 
    else:
      #  print line.strip()
        if regex_latin2:
            if df_min=="?" and df_max == "?":
                dose_frequency = convert(regex_latin2.group())
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',dose_frequency,'|',dose_frequency,'|',required,'|',du,'|',cod)+"\n") 
            elif df_min=="0" and df_max == "?":
                dose_frequency = convert(regex_latin2.group())
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|',dn_min,'|',dn_max,'|',"0",'|',dose_frequency,'|',required,'|',du,'|',cod)+"\n")
            else:
#                print line.strip()
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|',dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")
        else:
            if "oml" in df_min or "oml" in df_max :
                if regex_times2:
                    if regex_oml2 and required=="yes":
                        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"0",'|',"1",'|',required,'|',du,'|',cod)+"\n") 
                    elif regex_oml2 and required=="no":
                        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"1",'|',"1",'|',required,'|',du,'|',cod)+"\n") 
                    else:
                        if required=="yes":
                            df = convert(regex_times2.group(1))
                            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"0",'|',df,'|',required,'|',du,'|',cod)+"\n") 
                        else:
                            df = convert(regex_times2.group(1))
                            frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df,'|',df,'|',required,'|',du,'|',cod)+"\n") 
                else:
                    if required=="yes": ## I put ? here in df_max because these few cases have no information whatsover
                        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"0",'|',"?",'|',required,'|',du,'|',cod)+"\n")
                    else:
                        frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"?",'|',"?",'|',required,'|',du,'|',cod)+"\n")
            else:
                frequency_dose_file.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n") 
frequency_dose_file.close()


frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:5}{5:2}{6:5}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format('text_id','|','text', '|', 'DN_min','|','DN_MAX','|','DF_MIN','|','DF_MX','|','required?','|','DU','|','COD')+"\n")  


for line in open(sys.argv[2],'r'):
    if "text_id" in line:
        continue
    info = line.split('|')
    text = info[0].strip()
    information = info[1].strip().lower()
    dn_min = info[2].strip()
    dn_max = info[3].strip()
    df_min = info[4].strip()
    df_max = info[5].strip()
    required = info[6].strip()
    du = info[7].strip()
    cod = info[8].strip()
    regex_freq = re.compile('([1-9]+|[0-9]+\.[0-9]+)')
    regex_verb = re.compile('(apply|use|inject|suck|spray|instil|chew|inhale|insert|put|take|add|instilled|taken|chewed|inserted|injected|sucked|sprayed|inhaled|applied|used|added|dissolved)')
    regex_verb_single = re.compile('(?:apply|use|inject|suck|spray|instil|chew|inhale|insert|put|take|add|instilled|taken|chewed|inserted|injected|sucked|sprayed|inhaled|applied|used|added|dissolved)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)')
    regex_freq2 = re.search(regex_freq, df_min)
    regex_freq3 = re.search(regex_freq, df_max)
    regex_verb2 = re.search(regex_verb, information)
    regex_verb_single2 = re.search(regex_verb_single, information)
    regex_daily = re.compile('day|daily|dly|evening|morning|afternoon|noon|tea\stime|teatime|dusk|dawn|eve|night|midnight|morne|nocte|noct|morn|bedtime|after\smeals|after\sbreakfast|after\slunch|after\sdinner|dinner\stime|lunch\stime|dai|midday')
    regex_daily2 = re.search(regex_daily, information)
    if df_min == "0" and df_max == "0" and dn_min == "0" and dn_max=="0" and required=="yes":
   #     print line.strip()
# here we are making the dose number min and max = 1 since there is some info/wording in the sentence:p
        frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|',"1",'|',df_min,'|',"?",'|',required,'|',du,'|',cod)+"\n") 



    elif (df_min!="0" or df_min=="0") and df_max!= "0" and dn_min=="0" and dn_max=="0" and required=="no": 
# we have here dose frequency # than zero but not dose number. this is by default then into 1
      #  print line.strip()
        frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|',"1",'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")



    elif (df_min!="0" or df_min=="0") and df_max!= "0" and dn_min=="0" and dn_max=="0" and required=="yes": 
# we have here dose frequency # than zero but not dose number. this is by default then into 1
#        print line.strip()
        regex_letter = re.compile('([a-z])')
        regex_letter_df_max = re.search(regex_letter, df_max)
        if regex_letter_df_max:
         #   print line.strip()
            frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|',"1",'|',df_min,'|',"?",'|',required,'|',du,'|',cod)+"\n")            
        else:
            frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|',"1",'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")



    elif (df_min!="0" or df_min=="0" and df_min!="?") and (df_max!= "0" and df_max!="?") and dn_min=="?" and dn_max=="?" and required=="no": 
# we have here dose frequency # than zero but not dose number. this is by default then into 1
       # print line.strip()
        frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|',"1",'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")


    elif dn_min!="0" and dn_max!="0" and df_min == "0" and df_max=="0" and required=="yes": 
# here we have dose number but the frequency is zero - zero is converted into ?
#        print line.strip()
        frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"0",'|',"?",'|',required,'|',du,'|',cod)+"\n")



    elif dn_min!="0" and dn_max!="0" and df_min == "0" and df_max=="0" and required=="no": 
# here we have dose number but the frequency is zero - zero is converted into ?
#        print line.strip()
        frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"?",'|',"?",'|',required,'|',du,'|',cod)+"\n")


    elif df_min == "0" and df_max == "0" and dn_min == "0" and dn_max=="0" and required=="no": #everything is here zero.
  #      print line.strip()
        if regex_verb2: # the moment there is a verb put dn 1.
           # print line.strip()
            frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|',"1",'|',"?",'|',"?",'|',required,'|',du,'|',cod)+"\n")
        else: # else put ????
#            print line.strip()
##defaulting those who have everything zero with ?
            if "directed" in information:
                frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "1",'|',"1",'|',"?",'|',"?",'|',required,'|',du,'|',cod)+"\n")
            else:
          #      print line.strip() ###################useless prescriptions
                frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', "?",'|',"?",'|',"?",'|',"?",'|',required,'|',du,'|',"?")+"\n")

    elif dn_min!="0" and dn_min!="?" and dn_max!="0" and dn_max !="?" and df_min == "?" and df_max=="?" and required=="no":
    #    print line.strip()
        if regex_daily2:
            frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',"1",'|',"1",'|',required,'|',du,'|',cod)+"\n")
        else:
            frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")

    else:
      #  print line.strip()
        regex_letter = re.compile('([a-z])')
        regex_letter_df_min = re.search(regex_letter, df_min)
        regex_letter_df_max = re.search(regex_letter, df_max)
        if regex_letter_df_min and regex_letter_df_max:
            frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_min,'|',"?",'|',"?",'|',required,'|',du,'|',cod)+"\n")
        elif regex_letter_df_max and df_min =="0":
            frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_min,'|',"0",'|',"?",'|',required,'|',du,'|',cod)+"\n")
        elif dn_min=="?" and dn_max=="?" and regex_verb_single2:
            dn_min = convert(regex_verb_single2.group(1))
            frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_min,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")
        else:
            frequency_dose_file2.write("{0:7}{1:2}{2:70}{3:2}{4:6}{5:2}{6:6}{7:2}{8:7}{9:2}{10:6}{11:2}{12:5}{13:2}{14:7}{15:2}{16:}".format(text,'|',information, '|', dn_min,'|',dn_max,'|',df_min,'|',df_max,'|',required,'|',du,'|',cod)+"\n")
frequency_dose_file2.close()
