#!usr/local/python

import sys
import re

frequency_dict = {"once":"1", "twice":"2", "three":"3", "four":"4", "five":"5","six":"6","seven":"7", "eight":"8","nine":"9","ten":"10","eleven":"11","twelve":"12", "bd":"2","b. d":"2","b.d.":"2","b. d.":"2","b.d":"2","t.d.s":"3","t.d.s.":"3","t. d. s.":"3", "tds":"3","t.i.d":"3","t.i.d.":"3","t. i. d.":"3", "tid":"3", "tiw":"3", "t.i.w":"3","t.i.w.":"3","t. i. w.":"3","sid":"1","s.i.d":"1","s.i.d.":"1","q i d":"4","t d":"3","b d":"2","t i d":"3","s. i. d.":"1", "qwk":"1", "q.w.k":"1","q.w.k.":"1","q. w. k.":"1","qqh":"6", "q.q.h" :"6","q.q.h." :"6","q. q. h." :"6","qod":"1", "q.o.d":"1","q.o.d.":"1","q. o. d.":"1", "qid":"4", "q.i.d":"4","q.i.d.":"4","q. i. d.":"4", "qd":"1", "q.d":"1","q.d.":"1","q. d.":"1", "q1d":"1", "q.1.d":"1","q.1.d.":"1","q. 1. d.":"1","am":"1","a.m":"1","a.m.":"1","a. m.":"1", "bis":"2", "b.i.s":"2","b.i.s.":"2","b. i. s.":"2","bid":"2", "b.i.d":"2","b.i.d.":"2","b. i. d.":"2","bt":"1","b.t.":"1","b. t.":"1", "b.t":"1", "hs":"1", "h.s":"1","h.s.":"1","h. s.":"1", "dieb alt":"1","alt":"1","eod":"1","e.o.d":"1","e.o.d.":"1","e. o. d.":"1","mane":"1","on":"1","o.n":"1","o.n.":"1","t. d. s.":"3","o. n.":"1","om":"1","o.m":"1","o.m.":"1","o. m.":"1","opd":"1","o.p.d":"1","o.p.d.":"1","o. p. d.":"1","pm":"1","p.m":"1","p.m.":"1","p. m.":"1","two":"2","qad":"1","q.a.d":"1","q.a.d.":"1","q. a. d.":"1","qam":"1","q.a.m":"1","q.a.m.":"1","q. a. m.":"1","od":"1","o.d":"1","qds":"4","q.d.s":"4","q.d.s.":"4","q. d. s.":"4","qpm":"1","q.p.m":"1","q.p.m.":"1","q. p. m.":"1","qh":"24","q.h":"24","q.h.":"24","q. h.":"24","qhs":"1","q.h.s":"1","q.h.s.":"1","q. h. s.":"1","q1h":"24", "q.1.h":"24","q.1.h.":"24","q. 1. h.":"24","q2h":"12","q.2.h":"12","q.2.h.":"12","q. 2. h.":"12", "nocte":"1","noct":"1","bds":"2","b.d.s":"2","b.d.s.":"2","b. d. s.":"2", "t.d":"3","t.d.":"3","t. d.":"3", "td":"3", "qh":"24", "q.h":"24","q.h.":"24","q. h.":"24","alt sh":"12",
"q3h":"8","q4h":"6","q5h":"4.8","q6h":"4","q7h":"3.4","q8h":"3","q.3.h":"8","q.4.h":"6","q.5.h":"4.8","q.6.h":"4","q.7.h":"3.4","q.8.h":"3","q.3.h.":"8","q.4.h.":"6","q.5.h.":"4.8","q.6.h.":"4","q.7.h.":"3.4","q.8.h.":"3", "eve":"1", "morning":"1","night": "1", "day":"1", "afternoon":"1", "evening":"1", "one":"1", "midday":"1", "midnight":"1", "teatime":"1", "dusk":"1", "bedtime":"1", "mor":"1", "dawn":"1", "morne":"1",  "morn":"1", "each":"1", "every":"1","twelve":"12", "eleven":"11", "thirteen":"13", "fourteen":"14", "fifteen":"15", "sixteen":"16", "seventeen":"17", "nineteen":"19", "eighteeen":"18", "twenty":"20", "twenty one":"21", "twenty two":"22", "twenty three":"23", "twenty four":"24", "daily":"1", "a month":"1", "tea time":"1", "noon":"1", "nightly":"1", "lunchtime":"1", "lunch time":"1", "bet time":"1", "dinnertime":"1", "dinner time":"1", "other":"2", "twice/":"2", "thrice":"3"}

def convert(n): 
    if n in frequency_dict:
        return frequency_dict[n]
    else:
        return n
    
regex_every_days = re.compile('(every|each)\s([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|sixteen|fifteen|seventeen|eighteen|nineteen|twenty)\s(days|day|month|months|weeks|wks|week|wk|years|year|yrs|nights|night)')

regex_once = re.compile('once\s[a-z]')

regex_twice = re.compile('twice\s[a-z]')

regex_thrice = re.compile('thrice\s[a-z]')

regex_once_or_twice = re.compile('(once)\s(?:or|to|-|/)\s(twice)')

regex_every = re.compile('(every|each)\s[a-z]')

regex_hour = re.compile('(?:up)?(?:\s+)?(?:to)?(?:\s+)?(?:every|each)(?:\s+)?([0-9]+|[a-z]+)(?:\s+)?(?:hours|hrs|hour)')

regex_hr = re.compile('(?:up)?(?:\s+)?(?:to)?(?:\s+)?(?:every|each)(?:\s+)?([0-9]+|[a-z]+)(?:\s+)?(?:hr)')

regex_hours = re.compile('(?:every|each)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty+)(?:\s+)?(?:-|to|or)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty+)(?:\s+)?(?:hour|hours|hrs|hr)')

regex_hourly = re.compile('([0-9]+|[a-z]+)(?:\s+)?(?:-|to|or|/)(?:\s+)?([0-9]+|[a-z]+)(?:\s+)?(?:hourly|hly|hrly|hy)')

regex_word_hourly = re.compile('([a-z]+|[0-9]+)(?:\s+)?(?:-)?(?:hourly|hly|hrly|hy)')

regex_x_hourly = re.compile('(?:[0-9]+)(?:\s+)?(?:x)(?:\s+)?([0-9]+)(?:\s+)?(?:hourly|hly|hrly|hy)')

regex_every_hour = re.compile('(?:every|each)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)?(?:hours|hrs|hour|hr)')

regex_every_hour_double = re.compile('(?:every|each)(?:\s+)?([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:-|to|or|/)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:hours|hrs|hour)')

regex_ampm = re.compile('(?:in)(?:\s+)(am\Z|pm|a.m.|a.\sm.|a.m|p.m.|p.\sm.|p.m)')

regex_both_ampm = re.compile('(?:[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)?(am|pm|on|om)(?:\s+)?(?:[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)?(?:at|in|during)?(?:\s+)?(?:the|a|an)?(?:\s+)?(am|pm|on|om|morning|evening|afternoon|night|midnight|midday|day|mor|dusk|bedtime|eve|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)\s?')

regex_period_am = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)\s([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)(am|pm)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)(am|pm)')

regex_every_or = re.compile('([a-z]+|[0-9]+)(?:\s+)(?:morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)?(?:\s+)?(?:or|/|-|to)(?:\s+)([a-z]+|[0-9]+)(?:\s+)(?:a)(?:\s+)(?:morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)')

regex_every_and_every = re.compile('(?:[a-z]+|[0-9]+)(?:\s+)(?:every|each|at|during)(?:\s+)(morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)(?:\s+)(?:[a-z]+|[0-9]+)(?:\s+)(?:and)?(?:\s+)?(?:every|each|at|during)(?:\s+)(?:the)?(?:\s+)?(morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)')

regex_perday = re.compile('([0-9]+|[a-z]+)\s?per\s(day|night|noon|afternoon|eve|evening|morning|morn|mor)')

regex_inthe = re.compile('(?:[0-9]+|[a-z]+)(?:\s+)(?:in|a|an|at|every|each|per)?(?:\s+)?(?:the|a|an)?(?:\s+)?(morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)(?:\s+)?(?:and)?(?:\s+)?(?:[0-9]+|[a-z]+)(?:\s+)(?:in|at|every|each|per|a|an)?(?:\s+)?(?:the)?(?:\s+)?(morning|evening|afternoon|night|midnight|midday|day|mor|dusk|bedtime|eve|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)')

regex_verb_period = re.compile('(?:apply|chew|take|insert|use|instil|inject|suck|spray|inhale|dissolve|put)(?:\s+)?(morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|breakfast|dinner|lunch|supper|dinnertime|dinner\stime|lunchtime|lunch\stime|bed|bed\stime)(?:\s+)?(?:and)(morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|breakfast|dinner|lunch|supper|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)')

regex_verb_dose_number_period = re.compile('(?:apply|chew|take|insert|use|instil|inject|suck|spray|inhale|dissolve|put)(?:\s+)?([0-9]+|[a-z]+)(?:morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|breakfast|dinner|lunch|supper|nightly|daily|dlydinnertime|dinner\stime|lunchtime|lunch\stime|bed|bed\stime)')

regex_latin = re.compile('(qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am\Z|pm|bid|bt|hs|dieb\salt|eod|mane|\Aonprn|on\Z|om\Z|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct|b.\sd|q3h|q4h|q5h|q6h|q7h|q8h|alt)')

regex_nospaces = re.compile('(?:[0-9]+)(?:\s+)?(?:ml|mls|msl|puffs|puff|puf|pufs|table|tablets|tabs|tab|capsules|capsule|caps|cap|pastille|pastilles|sachets|sachet|pills|pill|drop|drps|drops|blister|blisters|amps|ampoule|ampoules|amp|sprays|spray|grams|gram|micrograms|microgram|gm|gms|gs|mcgs|mcg|unit|units|milligrams|milligram|mgs|mg|suppositor|suppository|suppos|ptch|patches|ounces|ounce|lozenge|lozenges|losenge|losenges|millilitre|millilitres|packs|packets|pack|packet)(?:\s+)?(\Aqds|\Atds|\Abd|\Atid|\Atiw|\Abis|\Asid|\Aqwk|\Aqqh|\Aqod|\Aqid|\Aqd|\Aq1d|\Aam|\Apm|\Abid|\Abt|\Ahs|\Adieb alt|\Aeod|\Amane|on\Z|\Aom|\Aopd|\Aqad|\Aqam|\Aqpm|\Aqh|\Aqhs|\Aq1h|\Aq2h|\Anocte|\Atd|\Anoct|\Aq.d.s|\At.d.s|\Ab.d|\At.i.d|\Ab.i.s|\As.i.d|\Aq.w.k|\Aq.q.h|\Aq.o.d|\Aq.i.d|\Aq.d|\Aq.1.d|\Aa.m|\Ap.m|\Ab.i.d|\Ab.t|\Ah.s|\Adieb.alt|\Ae.o.d|\Ao.n|\Ao.m|\Ao.d|\Ao.p.d|\Aq.a.d|\Aq.a.m|\Aq.p.m|\Aq.h|\Aq.h.s|\Aq.2.h|\Ao.p|\At.d|\Aq.d.s.|\At.d.s.|\Aq3h|\Aq4h|\Aq5h|\Aq6h|\Aq7h|\Aq8h|\Aq.3.h|\Aq.4.h|\Aq.5.h|\Aq.6.h|\Aq.7.h|\Aq.8.h|\Aq.3.h.|\Aq.4.h.|\Aq.5.h.|\Aq.6.h.|\Aq.7.h.|\Aq.8.h.)')

regex_times = re.compile('([0-9]+|[a-z]+)(?:\s+)?(?:times)?(?:\s+)?(?:a)?(?:\s+)?(?:day)?(?:\s+)?(?:or|to|-|/)(?:\s+)?([0-9]+|[a-z]+)(?:\s+)(?:times)(?:\s+)(?:a)(?:\s+)(?:day)')

regex_onlytimes = re.compile('(?:times)(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)(?:every|each|at|on|during|before|after)(?:\s+)(?:morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)')

regex_latin_or = re.compile('(qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am\Z|pm|bid|bt|hs|dieb\salt|eod|mane|on\Z|om|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct)(?:\s+)(?:or|to|/|-)(?:\s+)(qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am\Z|pm|bid|bt|hs|dieb\salt|eod|mane|on\Z|om|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct|q3h|q4h|q5h|q6h|q7h|q8h)')

regex_latin_or_numbers = re.compile('(?:[a-z]|[0-9]+)(?:\s+)?(qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am|pm|bid|bt|hs|dieb\salt|eod|mane|on\Z|om|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct)(?:\s+)?(?:or|to|/|-)?(?:\s+)?(?:[a-z]|[0-9]+)(?:\s+)?(qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am\Z|pm|bid|bt|hs|dieb\salt|eod|mane|on\Z|om|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct|q3h|q4h|q5h|q6h|q7h|q8h)')##put an extract ? sto keno prin to or

regex_double_latin = re.compile('(qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am|pm|bid|bt|hs|dieb\salt|eod|mane|on\Z|om|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct)(?:\s+)?(?:or|to|/|-)(?:\s+)?(qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am\Z|pm|bid|bt|hs|dieb\salt|eod|mane|on\Z|om|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct|q3h|q4h|q5h|q6h|q7h|q8h)')

regex_ml_only = re.compile('(?:[0-9+|[a-z]+)(?:\s+)?(?:ml|mls|msl)(?:\s+)?(qds|tds|bd|tid|tiw|bis|sid|qwk|qqh|qod|qid|qd|q1d|am\Z|pm|bid|bt|hs|dieb\salt|eod|mane|on\Z|om|opd|qad|qam|qpm|qh|qhs|q1h|q2h|nocte|td|noct|q3h|q4h|q5h|q6h|q7h|q8h)')

regex_meals = re.compile('(?:before|after|with|at|qac|between)(?:\s+)(meals|meal|food|breakfast|dinner|supper|lunch|evening\smeal)(?:\s+)(?:and|\+)(?:\s+)(at|every|each|a|an|in)?(?:\s+)?(?:the)?(?:\s+)?(?:morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|teatime|noon|tea\stime|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)')

regex_meals_freq = re.compile('(?:at|every|each|a|an)(?:\s+)?(?:morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|tea time|teatime|midday|teatime|noon|tea\stime|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)(?:\s)(?:before|after|with|at|qac|between)(?:\s+)(meals|meal|food|breakfast|dinner|supper|lunch|evening\smeal)')

regex_double_meal = re.compile('(?:[0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:[a-z]+)(?:\s+)?(main\smeal|meal|dinner|breakfast|lunch|supper|food|evening\smeal)(?:\s+)?(?:and)(?:\s+)?(?:[0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:[a-z]+)(?:\s+)?(main\smeal|meal|dinner|breakfast|lunch|supper|food|evening\smeal)')

regex_freq = re.compile('([0-9]+|[a-z]+)(?:\s+)?(?:-|or|to)(?:\s+)?([0-9]+|[a-z]+)(?:\s+)(?:a|the|times)?(?:\s+)?(?:wk|week|wks|weekly|wkly|wly|weekley)')

regex_a_week = re.compile('([0-9]+|[a-z]+)(?:\s+)(?:times)(?:\s+)?(?:a)?(?:\s+)?(?:week|weekly|wkly|wk|wks|wly|weekley)')

regex_freq_monthly = re.compile('([0-9]+|[a-z]+)(?:\s+)?(?:-|or|to)(?:\s+)?([0-9]+|[a-z]+)(?:\s+)(?:a|the|times)?(?:\s+)?(?:monthly|month|mthly)')

regex_a_month = re.compile('([0-9]+|[a-z]+)(?:\s+)?(?:a|the|times)?(?:\s+)?(?:a)?(?:\s+)?(?:monthly|month|mthly)')

regex_every_month = re.compile('(?:every|each)(?:\s+)?([0-9+]+|[a-z]+)(?:\s+)?(?:months|month|mth)')

regex_every_week = re.compile('(?:every|each)(?:\s+)?([0-9]+|[a-z]+)(?:\s+)?(?:weeks|week|wk|wks)')

regex_double_number = re.compile('(?:[0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:or|-|to|/)(?:\s+)?(?:[a-z]+|[0-9]+|[0-9]+.[0-9]+)(?:\s+)?([a-z]+|[0-9]+)(?:\s+)?(?:times)')

regex_single_number = re.compile('(?:[0-9]+|[0-9]+.[0-9]+)(?:\s+)?([a-z]+|[0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:times)')

regex_single_time = re.compile('(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|[0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:time)(?:\s+)?(?:a|per|every|each)(?:\s+)(?:morning|evening|afternoon|night|midnight|midday|day|eve|mor|bedtime|dusk|dawn|morne|mane|nocte|noct|morn|tea time|teatime|midday|teatime|noon|tea\stime|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)')

regex_max_times = re.compile('(?:maximum|max|up\s+to|upto)(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:times|time)')

regex_alt_single_number = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:times|time)')

regex_dose_unit_period = re.compile('([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:cap|capsules|caps|unit|units|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|drops|drop|drps|drp|drs|dr|ampoule|ampoules|amps|amp|pastilles|pastille|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|mcg|mg|mgs|\Ag$|gs|ml|msl|millilitre|millilitres|packs|packets|pack|packet)(?:\s+)?(?:each|every|a|an|in|at|per)(?:\s+)?(?:the)?(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:each|every|a|an|in|at|per)(?:\s+)?(?:the)?(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)')

regex_dose_unit_period_info = re.compile('(?:[0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:cap|capsules|unit|units|caps|capsule|sachet|sachets|puf|puffs|puff|pastille|pastilles|tabs|tab|tablet|tablets|drops|drop|drps|drp|drs|dr|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|mcg|mg|mgs|\Ag$|gs|ml|msl|millilitre|millilitres|packs|packets|pack|packet)(?:\s+)?(?:[a-z]+)(?:\s+)(?:[a-z]+)(?:\s+)(?:each|every|a|an|in|at|per)(?:\s+)?(?:the)?(?:\s+)?(morning|mor|morn|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:each|every|a|an|in|at|during|after|before)?')

regex_q_multiple = re.compile('(?:q)([0-9]+)(?:-)([0-9]+)(?:h)?')

regex_q_single = re.compile('(?:q)([0-9]+)(?:h)?')

dose_number_regex = re.compile('(?:[0-9]|[a-z]+)(?:\s+)?(?:/|-|or|to)(?:\s+)?(?:[0-9]|[a-z]+)(?:\s+)?(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|[0-9])(?:\s+)?(?:times|time)(?:\s+)?(?:a)(?:\s+)(?:day)')

regex_latin_spaces = re.compile('\At.\sd.\ss.|\Ab\sd|\Aq\si\sd|\At\sd|\At\si\sd')

regex_q_hours = re.compile('(?:q)(?:\s+)?([0-9]+)(?:\s+)?(?:hrs|hr|h)')

regex_in_the_morning = re.compile('([a-z]+|[0-9]+)(?:\s+)?(?:in)(?:\s+)(?:the)(?:\s+)?(morning|mor|morn|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)(?:\s+)?(?:after|with)')

regex_in_the_morning_double = re.compile('([a-z]+|[0-9]+)(?:\s+)?(?:in)(?:\s+)(?:the)(?:\s+)?(morning|mor|morn|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)(?:\s+)?(?:and)(?:\s+)?([a-z]+)')

regex_verb = re.compile('take(?:\s+)?(?:[a-z]+|[0-9]+)(?:\s+)?([a-z]+)')

regex_frequency_dose_number = re.compile('(?:[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:-|to|or)(?:\s+)?(?:[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?([a-z]+|[0-9]+)(?:\s+)?(?:times|time)')

regex_two_periods_no_number = re.compile('(morning|mor|morn|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)(?:\s+)?(?:and)(?:\s+)?(?:in|at|during|after)?(?:\s+)?(?:the)?(?:\s+)?(morning|mor|morn|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)')

regex_double_meal_complicated = re.compile('(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|twenty|[0-9])(?:\s+)?(?:times|time)(?:\s+)?(?:each|every|a|an|in|at|per|during|after|before|with)(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)(?:\s+)?(?:[a-z]+)(?:\s+)?(?:main\smeal|meal|dinner|breakfast|lunch|supper|food|evening\smeal)(?:\s+)?(?:and)?(?:\s+)?(?:[0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:each|every|a|an|in|at|per|during|after|before|with)(?:\s+)?(morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)')

regex_number_hours = re.compile('([0-9]+)(?:\s+)?(?:hrs|hr|h|hours|hour)')

new_extracted_dose_number = open(sys.argv[2], 'w')

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

frequency_flag=0
for line in open(sys.argv[1],'r'): # here you are opening the extracted information from minorthird
    if "dose_frequency\n"==line:
        frequency_flag = 1
        new_extracted_dose_number.write("dose_frequency"+"\n")
        continue
    if frequency_flag==1:
        txt = line.find('.txt')
        txt_id = line[:txt+4].strip()
        info = line[txt+5:].strip()
        regex_once2 = re.search(regex_once, info)
        regex_twice2 = re.search(regex_twice, info)
        regex_thrice2 = re.search(regex_thrice, info)
        regex_every2 = re.search(regex_every, info)
        regex_hour2 = re.search(regex_hour, info)
        regex_hr2 = re.search(regex_hour, info)
        regex_hours2 = re.search(regex_hours, info)
        regex_hourly2 = re.search(regex_hourly, info)
        regex_word_hourly2 = re.search(regex_word_hourly, info)
        regex_ampm2 = re.search(regex_ampm, info)
        regex_perday2 = re.search(regex_perday,info)
        regex_inthe2 = re.search(regex_inthe, info)
        regex_latin2 = re.search(regex_latin, info)
        regex_nospaces2 = re.search(regex_nospaces, info)
        regex_times2 = re.search(regex_times, info)
        regex_every_or2 = re.search(regex_every_or,info)
        regex_onlytimes2 = re.search(regex_onlytimes, info)
        regex_every_and_every2 = re.search(regex_every_and_every, info)
        regex_latin_or2 = re.search(regex_latin_or, info)
        regex_once_or_twice2 = re.search(regex_once_or_twice,info)
        regex_both_ampm2 = re.search(regex_both_ampm,info)
        regex_ml_only2 = re.search(regex_ml_only,info)
        regex_meals2 = re.search(regex_meals, info)
        regex_freq2 = re.search(regex_freq, info)
        regex_a_week2 = re.search(regex_a_week, info)
        regex_freq_monthly2 = re.search(regex_freq_monthly, info)
        regex_a_month2 = re.search(regex_a_month, info)
        regex_meals_freq2= re.search(regex_meals_freq,info)
        regex_x_hourly2 = re.search(regex_x_hourly,info)
        regex_single_number2 = re.search(regex_single_number, info)
        regex_double_number2 = re.search(regex_double_number, info)
        regex_alt_single_number2 = re.search(regex_alt_single_number,info)   
        regex_max_times2 = re.search(regex_max_times, info)    
        regex_dose_unit_period2 = re.search(regex_dose_unit_period, info)
        regex_dose_unit_period_info2 = re.search(regex_dose_unit_period_info, info) 
        regex_double_meal2 = re.search(regex_double_meal, info)
        regex_every_month2 = re.search(regex_every_month, info)
        regex_every_week2 = re.search(regex_every_week, info)
        regex_verb_period2 = re.search(regex_verb_period, info)
        regex_q_single2 = re.search(regex_q_single,info)
        regex_q_multiple2 = re.search(regex_q_multiple,info)
        dose_number_regex2 = re.search(dose_number_regex,info)
        regex_latin_or_numbers2 = re.search(regex_latin_or_numbers, info) 
        regex_every_hour2 = re.search(regex_every_hour, info)
        regex_every_hour_double2 = re.search(regex_every_hour_double, info)
        regex_verb_dose_number_period2 = re.search(regex_verb_dose_number_period,info)
        regex_latin_spaces2 = re.search(regex_latin_spaces, info)
        regex_q_hours2 = re.search(regex_q_hours, info)
        regex_in_the_morning2 = re.search(regex_in_the_morning, info)
        regex_in_the_morning_double2 = re.search(regex_in_the_morning_double, info)
        regex_verb2 = re.search(regex_verb, info)
        regex_frequency_dose_number2 = re.search(regex_frequency_dose_number, info)
        regex_two_periods_no_number2 = re.search(regex_two_periods_no_number, info)
        regex_period_am2 = re.search(regex_period_am , info) 
        regex_single_time2 = re.search(regex_single_time, info)
        regex_double_meal_complicated2 = re.search(regex_double_meal_complicated, info)
        regex_every_days2 = re.search(regex_every_days,info)
        regex_number_hours2 = re.search(regex_number_hours, info)
        regex_double_latin2 = re.search(regex_double_latin, info) 
        if "weekly" == info or "monthly"==info or "wkly"==info or "in the week"==info or "in a week"==info or "a week" ==info or "wk"==info or "a month"==info:
            line = txt_id + " " + "?"#/7"
        elif "week" in info or "wk" in info:
            if regex_freq2:
                dose_freq1 = convert(regex_freq2.group(1)) #+"/7"
                dose_freq2 = convert(regex_freq2.group(2)) #+"/7"
                line = txt_id + " " + dose_freq1 + "-" + dose_freq2
            elif regex_every_week2:
                line = txt_id + " "+"1"#/7"
            elif regex_a_week2:
                dose_frequency = convert(regex_a_week2.group(1))
                if dose_frequency == "per" or dose_frequency == "times" or dose_frequency == "time":
                    line = txt_id + " " + "1"#+"/7"
                else:
                    line = txt_id + " " + dose_frequency#+"/7"
            else:
                if "twice" in info:
                    line = txt_id + " " + "2"
                else:
                    line = txt_id + " "+"1"#/7"
        elif "month" in info or "mthly" in info or "mnthly" in info:
            if regex_freq_monthly2:
                dose_freq1 = convert(regex_freq_monthly2.group(1))
                dose_freq2 = convert(regex_freq_monthly2.group(2))
                line = txt_id + " " + dose_freq1 + "-" + dose_freq2
            elif regex_a_month2:
                if regex_every_month2:
                    line = txt_id + " " + "1"
                else:
                    if "per" in info:
                        line = txt_id + " " + "1"#+"/30"
                    else:
                        dose_frequency = convert(regex_a_month2.group(1))
                        line = txt_id + " " + dose_frequency#+"/30"
            else:
                line = txt_id + " " + "1"#/30"
        elif regex_double_meal_complicated2:
        #    print line.strip()
            dose_freq_1 = convert(regex_double_meal_complicated2.group(1))
            dose_freq_2 = convert(regex_double_meal_complicated2.group(2))
            total_freq = int(dose_freq_1) + int(dose_freq_2)
            line = txt_id + " " + str(total_freq)
        elif regex_verb_period2:
           # print line.strip()
            line = txt_id + " " + "2"#/30"
        elif regex_verb_dose_number_period2:
           # print line.strip()
            line = txt_id + " " + "1"
        elif "times" in info:
           # print line.strip()
            if regex_max_times2: ## maximum four times per day
            #    print line.strip()
                dose_frequency_1 = convert(regex_max_times2.group(1))
                line = txt_id + " " + "1" + "-"+ dose_frequency_1
             #   print line
            elif regex_times2:
              #  print info
                dose_frequency_1 = convert(regex_times2.group(1))
                dose_frequency_2 = convert(regex_times2.group(2))
                line = txt_id + " " + comp(dose_frequency_1, dose_frequency_2)
            elif dose_number_regex2:
                dose_frequency_1 = convert(dose_number_regex2.group(1))
                line = txt_id + " " + dose_frequency_1
            elif regex_onlytimes2:
                dose_frequency_1 = convert(regex_onlytimes2.group(1))
                line = txt_id + " " + dose_frequency_1
            elif regex_single_number2:
                if regex_double_number2:
                    dose_frequency = convert(regex_double_number2.group(1))
                    line = txt_id + " " + dose_frequency
                else:
                    if regex_alt_single_number2:
                        dose_frequency = convert(regex_alt_single_number2.group(1))
                        line = txt_id + " " + dose_frequency
                    else:   
                        dose_frequency = convert(regex_single_number2.group(1))
                        line = txt_id + " " + dose_frequency                     
            else:
                if regex_frequency_dose_number2:
                    dose_frequency = convert(regex_frequency_dose_number2.group(1))
                    line = txt_id + " " + dose_frequency
                else:
                    boundary = info.find('times')
                    actual_frequency = info[:boundary]
                    line = txt_id + " " + actual_frequency
        elif regex_single_time2:
        #    print line.strip()
            actual_frequency = convert(regex_single_time2.group(1))
            line = txt_id + " " + actual_frequency 
        elif regex_dose_unit_period_info2:
        #    print line.strip()
            line = txt_id + " " + "2"
        elif regex_every_or2:
#            print line.strip()
            if "up" in info:
               # print line.strip()
                dose_frequency_2 = convert(regex_every_or2.group(2))
                line = txt_id + " " + "1-"+dose_frequency_2
            else:
              #  print line.strip()
                if "at" in info:
                    dose_frequency_2 = convert(regex_every_or2.group(2))
                    line = txt_id + " " + comp("1", dose_frequency_2)
                else:
                    dose_frequency_1 = convert(regex_every_or2.group(1))
                    dose_frequency_2 = convert(regex_every_or2.group(2))
                    line = txt_id + " " + comp(dose_frequency_1, dose_frequency_2)
        elif regex_every_and_every2:
#            print line.strip()
            dose_frequency_1 = convert(regex_every_and_every2.group(1))
            dose_frequency_2 = convert(regex_every_and_every2.group(2))
            total_frequency = int(dose_frequency_1) + int(dose_frequency_2)
            line = txt_id + " " + str(total_frequency)   
        elif regex_dose_unit_period2:
            print line.strip()
            line = txt_id + " " + "2"   
        elif regex_period_am2:
       #     print line.strip() 
            dose_frequency_1 = convert(regex_period_am2.group(1))
            dose_frequency_2 = convert(regex_period_am2.group(2))
            total_frequency = int(dose_frequency_1) + int(dose_frequency_2)
            line = txt_id + " " + str(total_frequency)   
        elif regex_both_ampm2:
      #      print line.strip()
            dose_frequency_1 = convert(regex_both_ampm2.group(1))
            dose_frequency_2 = convert(regex_both_ampm2.group(2))
            total_frequency = int(dose_frequency_1) + int(dose_frequency_2)
         #   print total_frequency
            line = txt_id + " " + str(total_frequency) 
        elif regex_perday2:
     #       print line.strip()
            actual_dose_frequency = regex_perday2.group(1)
            line = txt_id + " " + actual_dose_frequency
        elif regex_hours2:
    #        print line.strip()
            hour_1 = float(convert(regex_hours2.group(1)))
            hour_2 = float(convert(regex_hours2.group(2)))
            actual_dose_frequency_min = hour_strip(hour_2)
            actual_dose_frequency_max = hour_strip(hour_1)
            line = txt_id + " " + actual_dose_frequency_min + "-" + actual_dose_frequency_max
        elif regex_hour2:
            #print line.strip()
            if "up" in info:
                hour_1 = float(convert(regex_hour2.group(1)))
                if hour_1 > float(24):
                    line = txt_id + " " + "1"
                else:
                    actual_dose_frequency = hour_strip(hour_1)
                    line = txt_id + " " + "0"+ "-" + actual_dose_frequency
            else:
               # print line.strip()
                if regex_hour2.group(1) == "few":
## here I initialize the few with 3-4 hours
                    actual_dose_frequency_min = float(24)/float(4)
                    actual_dose_frequency_max = float(24)/float(3)
                    actual_dose_frequency_min = no_zero(actual_dose_frequency_min)
                    actual_dose_frequency_max = no_zero(actual_dose_frequency_max)
                    line = txt_id + " " + actual_dose_frequency_min + "-" + actual_dose_frequency_max
                else:
                    if float(convert(regex_hour2.group(1))) > float(24):
                        line = txt_id + " " + "1"
                    else:
                        hour_1 = convert(regex_hour2.group(1))
                        actual_dose_frequency = hour_strip(hour_1)
                        line = txt_id + " " + actual_dose_frequency
        elif regex_hourly2:
#            print line
            hour_1 = float(convert(regex_hourly2.group(1)))
            hour_2 = float(convert(regex_hourly2.group(2)))
            actual_dose_frequency_min = hour_strip(hour_2)
            actual_dose_frequency_max= hour_strip(hour_1)
            line = txt_id + " " + actual_dose_frequency_min + "-" + actual_dose_frequency_max
        elif regex_x_hourly2:
         #   print line
            actual_dose_frequency = regex_x_hourly2.group(1)
            actual_dose_frequency = hour_strip(actual_dose_frequency)
            line = txt_id + " " + actual_dose_frequency
        elif regex_word_hourly2:
        #    print line.strip()
            actual_dose_frequency = convert(regex_word_hourly2.group(1))
            actual_dose_frequency = hour_strip(actual_dose_frequency)
            line = txt_id + " " + actual_dose_frequency
        elif regex_inthe2:
           # print line.strip()
            generic = re.compile('([0-9]+|[a-z]+)(\s+)?(every|each|per|the|a|an)(\s+)?(morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)(\s+)?(with|during|after|before)(\s+)?(evening\smeals|evening\smeal\dinner|lunch|breakfast|food|meal|meals)')
            generic2 = re.search(generic, info)
            if "twice" in info:
                line = txt_id + " " + "3"
            elif generic2:
                line = txt_id + " " + "1" 
            else:
                line = txt_id + " " + "2" 
        elif regex_latin_or_numbers2:
          #  print line.strip()
            dose_frequency_1 = convert(regex_latin_or_numbers2.group(1))
            dose_frequency_2 = convert(regex_latin_or_numbers2.group(2))
            line = txt_id + " " + comp(dose_frequency_1, dose_frequency_2)
        elif regex_latin_or2:
          #  print line.strip()
            dose_frequency_1 = convert(regex_latin_or2.group(1))
            dose_frequency_2 = convert(regex_latin_or2.group(2))
            line = txt_id + " " + dose_frequency_1 + "-" + dose_frequency_2
            line = txt_id + " " + comp(dose_frequency_1, dose_frequency_2)
        elif regex_double_latin2:
       #      print line.strip()
             actual_dose_frequency_min = convert(regex_double_latin2.group(1))
             actual_dose_frequency_max = convert(regex_double_latin2.group(2))
             line = txt_id + " " + actual_dose_frequency_min + "-" + actual_dose_frequency_max    
        elif regex_latin2:
          #  print line.strip()
            if "on"==info:
                actual_dose_frequency = convert(regex_latin2.group())
                line = txt_id + " " + actual_dose_frequency 
            elif "on" in info:
                regex_hour_ampm = re.compile('([a-z]+|[0-9]+)(?:\s+)?(in|at|every|each)?(?:\s+)?(the)?(?:\s+)?([0-9]+|[a-z]+)?(?:\s+)?(morning|day|evening|am|pm|mane)?(?:\s+)?(and)?(?:\s+)?([0-9]+|[a-z]+)?(?:\s+)?(in|at|every|each)?(?:\s+)?([a-z]+|[0-9]+)?(?:\s+)?(am\Z|pm|night|mane|noon)')
                regex_hour_ampm2 = re.search(regex_hour_ampm, info)
                if regex_hour_ampm2:
                    line = txt_id + " " + "2" 
                elif "bd" in info:
                    line = txt_id + " 2" 
                elif "tds"  in info:
                    line = txt_id + " 3" 
                elif "twice" in info:
                    line = txt_id + " 3" 
                else:
                    line = txt_id + " 1" 
            else:
                if "alt" == info or "dieb alt"==info:
                #    print line.strip()
                    line = txt_id + " " + "?"
                else:
                    actual_dose_frequency = convert(regex_latin2.group())
                    line = txt_id + " " + actual_dose_frequency 
        elif regex_once_or_twice2:
       #     print line.strip()
            dose_frequency_1 = convert(regex_once_or_twice2.group(1))
            dose_frequency_2 = convert(regex_once_or_twice2.group(2))
            line = txt_id + " " + comp(dose_frequency_1, dose_frequency_2)
        elif regex_double_meal2:
        #    print line.strip()
            line = txt_id + " " + "2" 
        elif regex_meals2:
         #   print line.strip()
            necessary_information = regex_meals2.group(1)
            if "breakfast" in necessary_information or "supper" in necessary_information or "lunch" in necessary_information or "dinner" in necessary_information:
                line = txt_id + " " + "2"
            else:
                line = txt_id + " " + "4" 
        elif regex_meals_freq2:
          #  print line.strip()
            necessary_information = regex_meals_freq2.group(1)
            if necessary_information == "meals": 
                line = txt_id + " " + "3"
            else:
                if "twice" in line:
                    line = txt_id + " " + "2"
                else:
                    line = txt_id + " " + "1"                    
########################this is for the meals here. But I think it is too amgiguous. Setting the frequency as 3 is not a problem
        elif "meal" == info or "meals"==info or "feed" == info:
            line = txt_id + " " + "3"        
        elif "evening meal" ==info:
            line = txt_id + " " + "1"      
        elif regex_ml_only2:
           # print line.strip()
            dose_frequency_1 = convert(regex_ml_only2.group(1))
            line = txt_id + " " + dose_frequency_1              
        elif regex_once2:
         #   print line.strip()
            line = txt_id + " " + "1"
        elif regex_twice2:
          #  print line.strip()
            simple_regex = re.compile('(?:[0-9]+|[0-9]+.[0-9]|one|two|three|four|five|six|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|eighteen|twenty)(?:\s+)?(once|twice|every|each)(?:\s+)?(?:a|per)?(?:\s+)?(?:morning|mor|morn|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|daily|nightly|dai|dly|bed)(?:\s+)?(?:and|to)?(?:\s+)?(?:[0-9]+|[0-9]+.[0-9]|one|two|three|four|five|six|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|eighteen|twenty)(?:\s+)?(once|twice|every|each)?(?:\s+)?(?:at|per|a)?(?:\s+)?(morning|mor|morn|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|dinner\stime|lunchtime|lunch\stime|bed\stime|bed)')
            simple_regex2 = re.search(simple_regex,info)
            if "one daily" in info or "once daily" in info:
                line = txt_id + " " + "1-2"
            elif simple_regex2:
                line = txt_id + " " + "3"
            else:
                line = txt_id + " " + "2"
        elif regex_thrice2:
            line = txt_id + " " + "3"
        elif regex_every_hour_double2:
        #    print line.strip()
            hour_1 = float(convert(regex_every_hour_double2.group(1)))
            hour_2 = float(convert(regex_every_hour_double2.group(2)))
            actual_dose_frequency_min = hour_strip(hour_2)
            actual_dose_frequency_max = hour_strip(hour_1)
            line = txt_id + " " + actual_dose_frequency_min + "-" + actual_dose_frequency_max    
        elif regex_every_hour2:
         #   print line.strip()
            actual_dose_frequency = convert(regex_every_hour2.group(1))
            actual_dose_frequency = hour_strip(actual_dose_frequency)
            line = txt_id + " " + actual_dose_frequency
        elif regex_q_single2:
            if regex_q_multiple2:
                hour_1 = float(convert(regex_q_multiple2.group(1)))
                hour_2 = float(convert(regex_q_multiple2.group(2)))
                actual_dose_frequency_min = hour_strip(hour_2)
                actual_dose_frequency_max = hour_strip(hour_1)
                line = txt_id + " " + actual_dose_frequency_min + "-" + actual_dose_frequency_max                
            else:
                actual_dose_frequency = convert(regex_q_single2.group(1))
                actual_dose_frequency = hour_strip(actual_dose_frequency)
                line = txt_id + " " + actual_dose_frequency
        elif regex_hr2:
#            print line
            if "up" in info:
                hour_1 = float(convert(regex_hr2.group(1)))
                actual_dose_frequency = hour_strip(hour_1)
                line = txt_id + " " + "0"+ "-" + actual_dose_frequency
            else:
                hour_1 = float(convert(regex_hr2.group(1)))
                actual_dose_frequency = hour_strip(hour_1)
                line = txt_id + " " + actual_dose_frequency   
        elif regex_number_hours2:
#            print line
            hour_1 = float(convert(regex_number_hours2.group(1)))
            actual_dose_frequency = hour_strip(hour_1)
            line = txt_id + " " + actual_dose_frequency
        elif "od" in info:
            if "od"==info:
                line = txt_id + " " + "1"
            else:
                regex_od = re.compile('[0-9]\s?od\s?[0-9]\s?[a-z]')
                regex_od2 = re.search(regex_od, info)
                if regex_od2:
                    line = txt_id + " " + "2"
                else:
                    line = txt_id + " " + "1"
        elif "o.d." in info or "o.d" in info or "o. d." in info or "o. d" in info:
                line = txt_id + " " + "1"
        elif "op" in info or "omm" in info or "oon" in info or "o.p" in info or "o.p." in info or "o. p" in info or "o. p." in info:
       #     print line.strip()
            line = txt_id + " " + "?"
        elif regex_latin_spaces2:
          #  print line.strip()
          #  print regex_latin_spaces2.group(), txt_id
            dose_frequency = convert(regex_latin_spaces2.group())
            line = txt_id + " " + dose_frequency
        elif regex_q_hours2:
            hour_1 = float(convert(regex_q_hours2.group(1)))
            actual_dose_frequency = hour_strip(hour_1)
            line = txt_id + " " + actual_dose_frequency    
        elif regex_in_the_morning2:
        #    print line.strip()
            line = txt_id + " " + "1"
        elif regex_in_the_morning_double2:
           # print line.strip()
            line = txt_id + " " + "2"
        elif regex_verb2:
          #  print line.strip()
            line = txt_id + " " + "1"
        elif regex_two_periods_no_number2:
         #   print line.strip()
            line = txt_id + " " + "2"
        elif "every hour" == info or "every hr" == info:
           # print line.strip()
            line = txt_id + " " + "24"
        elif regex_every_days2:
       #     print line.strip() 
            line = txt_id + " " + "?"
        elif regex_every2 or "daily" == info or "daily" in info or "day" in info or "night" in info or "morn" in info or "evening" in info or "day"==info or "a day" == info or "in the morning"==info or "in the evening"==info or "in the afternoon"==info or "in the night"==info or "dly" == info or "in the day"==info or "at" in info or "eve" ==info or "nightly"==info or "a night"==info or "lunchtime" == info or "lunch time" == info or "dinnertime"== info or "dinner time" == info or "dly" in info or "bedtime" in info or "bed time" in info or "in evening" in info or "teatime" in info or "tea time" in info or "minute" in info or "every" in info and "day" in info or "per day" in info or "in morning" in info or "in evening" in info or "in night" in info or "in early evening" in info or "one a day with main meal" in info or "a day" in info or "bed" in info  or "per" in info:
           # print line.strip()
            line = txt_id + " " + "1"
    #    else:
          #  print line.strip()
    tokens = line.split()
    for i, word in enumerate(tokens):
        if word in frequency_dict:
            tokens[i] = frequency_dict[word]
    tokens2 = " ".join(tokens)
    if "upto" in tokens2:
        txt_boundary = line.find('.txt')
        txt_id = line[:txt_boundary+4]
        up_boundary = line.find('upto')
        times = convert(line[up_boundary+5:].strip())
        tokens2 = txt_id + " " + "1-" + times
    elif "up" in tokens2:
       # print line.strip()
        if "to" in tokens2:
            txt_boundary = line.find('.txt')
            txt_id = line[:txt_boundary+4]
            up_boundary = line.find('up to')
            times = line[up_boundary+6:].strip()
            if times =="several" or times =="many":
                tokens2 = txt_id + " " + "1-" + "?"       
            else:          
                times = convert(line[up_boundary+6:].strip())
                regex_number = re.compile('(?:upto|up\sto)(?:\s+)?([0-9]|one|two|three|four|five|six|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|eighteen|twenty)(?:\s+)?(?:-|to|or)(?:\s+)?(one|two|three|four|five|six|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|eighteen|twenty|[0-9])')
                regex_number2 = re.search(regex_number, tokens2)
                if regex_number2:
                    dose_freq_1 = convert(regex_number2.group(1))
                    dose_freq_2 = convert(regex_number2.group(2))    
                    tokens2 = txt_id + " " + str(dose_freq_1) + "-" + str(dose_freq_2)
                else:
                    if "suppos" in tokens2:
                        tokens2 = txt_id + " " + "1"
                    else:
                        tokens2 = txt_id + " " + "0-" + times
        else:
            txt_boundary = line.find('.txt')
            txt_id = line[:txt_boundary+4]
            up_boundary = line.find('up')
            times = convert(line[up_boundary+3:].strip())
            tokens2 = txt_id + " " + "1-" + times
    elif "to" in tokens2:
        txt_boundary = line.find('.txt')
        txt_id = line[:txt_boundary+4]
        up_boundary = line.find('to')
        times = line[up_boundary+3:].strip()
        tokens2 = txt_id + " " + "1-" + times
   # print tokens2
    new_extracted_dose_number.write(tokens2+"\n")
    if "dose_interval\n" in line:
        break
new_extracted_dose_number.close()
