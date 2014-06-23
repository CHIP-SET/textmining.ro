#!usr/local/python

import sys
import re

new_extracted_dose_number = open(sys.argv[2], 'w')

number_dict={"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "ten":"10", "apply":"1", "applied":"1","half":"0.5", "quarter":"0.25", "a":"1", "once":"1", "tablet":"1", "a half":"0.5", "eleven":"11","twelve":"12","thirteen":"13","fourteen":"14","fifteen":"15","sixteen":"16","seventeen":"17", "eighteen":"18","nineteen":"19","twenty":"20", "capsule":"1", "spray":"1", "drop":"1"}

def convert(n): #function that converts a word number into a number when it is called :P
    if n in number_dict:
        return number_dict[n]
    else:
        return n

regex2 = re.compile('[0-9]+d')
regex_latin = re.compile('([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:-|/|to|or)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:qwk|qqh|sid|bis|bos|qad|dieb\salt|eod|qh|qus|td|bd|bid|od|tid|tds|q1h|qhs|tiw|t.i.w|qd|qid|alt h|opd|op|om|on|nocte|qds|b.d|b.o.s|s.i.d|q.w.k|q.q.h|b.i.s|b.h|q.a.d|e.o.d|q.u.s|q.h|b.i.d|o.d|t.i.d|t.d.s|q.1.h|q.d|q.i.d|o.p.d|o.p|o.m|o.n|q.d.s|q.2.h|q2h|qod|q.o.d|q.h.s|q.h|qh|hs|h.s|mane|pm|p.m|bt|b.t|am|a.m|q1d|q.1.d|b.d.s|bds|q3h|q4h|q5h|q6h|q7h|q8h|q.3.h|q.4.h|q.5.h|q.6.h|q.7.h|q.8.h|q.3.h.|q.4.h.|q.5.h.|q.6.h.|q.7.h.|q.8.h.)')

regex_latin_single = re.compile('([0-9]+|[0-9]+.[0-9]+)\s?(?:-)?\s?(?:qwk|qqh|sid|bis|bos|qad|dieb alt|eod|qh|qus|td|bd|bid|od|tid|tds|q1h|qhs|tiw|t.i.w|qd|qid|alt h|opd|op|om|on|nocte|qds|b.d|b.o.s|s.i.d|q.w.k|q.q.h|b.i.s|b.h|q.a.d|e.o.d|q.u.s|q.h|b.i.d|o.d|t.i.d|t.d.s|q.1.h|q.d|q.i.d|o.p.d|o.p|o.m|o.n|q.d.s|q.2.h|q2h|qod|q.o.d|q.h.s|q.h|qh|hs|h.s|mane|pm|p.m|bt|b.t|am|a.m|q1d|q.1.d|b.d.s|bds|q3h|q4h|q5h|q6h|q7h|q8h|q.3.h|q.4.h|q.5.h|q.6.h|q.7.h|q.8.h|q.3.h.|q.4.h.|q.5.h.|q.6.h.|q.7.h.|q.8.h.)')

regex_other_day = re.compile('([0-9]+|[0-9]+\.[0-9]+)(?:\s+)?(?:every|each|alt|alternate|other)(?:\s+)?(?:day|eve|evening|morne|morning|morn|midnight|night|bedtime|teatime|dawn|noon|dusk|afternoon|noct|nocte|mane|dinner\stime|dinnertime|lunchtime|lunch\stime|noc)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:every|each)(?:\s+)?(?:other|alt|alternate)(?:\s+)?(?:day|eve|evening|morne|morning|morn|mor|midnight|night|bedtime|teatime|dawn|noon|dusk|afternoon|noct|nocte|mane|midday|tea\stime|dinner\stime|dinnertime|lunchtime|lunch\stime|noc)')

regex_two_periods = re.compile('([0-9]+|[0-9]+\.[0-9]+)(?:\s+)?(?:every|each|alt|alternate|other)(?:\s+)?(?:day|eve|evening|morne|morning|morn|midnight|night|bedtime|teatime|dawn|noon|dusk|afternoon|noct|nocte|mane|tea\stime|midday|dinner\stime|dinnertime|lunchtime|lunch\stime|noc)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:every|each)(?:\s+)?(?:day|eve|evening|morne|morning|morn|midnight|night|bedtime|teatime|tea\stime|midday|dawn|noon|dusk|afternoon|noct|nocte|mane|dinner\stime|dinnertime|lunchtime|lunch\stime|noc)')

regex_units_two = re.compile('([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:-|to|or|/)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|pastille|pastilles|drops|drop|drps|drp|drs|dr|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|mcg|mg|mgs|^g$|gs|millilitre|packs|packets|pack|packet|unit|units)')

regex_ampm = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:at|in)(?:\s+)?(?:[0-9]+)?(?:\s+)?(?:am|pm)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:at|in)(?:\s+)?(?:[0-9]+)?(?:\s+)?(?:am|pm)?')

regex_ml = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?([0-9]+)(?:\s+)?(?:ml|mls|millilitre|millilitres|milliliter)')


def no_zero(n):
    if ".0" in str(n):
        n = str(int(n))
    else:
        n = str(round(n,1))
    return n

for line in open(sys.argv[1],'r'):
    if "dose_number" in line:
        continue
    if "amount\n"==line:
        break
    text_id = line.find(".txt ")
    text_id2 = line[:text_id+4]
    info = line[text_id+4:].strip()
    regex4 = re.search(regex2, info)
    regex_latin2 = re.search(regex_latin, info)
    regex_latin_single2 = re.search(regex_latin_single, info)
    regex_other_day2 = re.search(regex_other_day,info)
    regex_two_periods2 = re.search(regex_two_periods, info)   
    regex_units_two2 = re.search(regex_units_two, info)
    regex_ampm2 = re.search(regex_ampm,info)
    regex_ml2 = re.search(regex_ml, info)
    if regex_units_two2:
  #      print line.strip()
        dose_number_min = regex_units_two2.group(1)
        dose_number_max = regex_units_two2.group(2)
        if float(dose_number_min) > float(dose_number_max):
            new_number1 = dose_number_max
            new_number2 = dose_number_min
            dose_number_min = new_number1
            dose_number_max = new_number2
            new_extracted_dose_number.write(text_id2 + " " + dose_number_min + "-" + dose_number_max +"\n")
        elif float(dose_number_min) == float(dose_number_max):
            new_extracted_dose_number.write(text_id2 + " " + dose_number_min + "-" + dose_number_max +"\n")
        else:
            new_extracted_dose_number.write(text_id2 + " " + dose_number_min + "-" + dose_number_max +"\n") 
    elif regex_ampm2:
#        print line.strip()
        number_1= convert(regex_ampm2.group(1))
        number_2 = convert(regex_ampm2.group(2))
        dose_number = int(number_1) + int(number_2)
        new_extracted_dose_number.write(text_id2 + " " + str(dose_number)+"\n")          
    elif regex4:
  #      print line.strip()
        dose_unit = info.find('d')
        dose_number = info[:dose_unit].strip()
        dose_number = dose_number.strip('-')
        dose_number = dose_number.strip('.')
        new_extracted_dose_number.write(text_id2 + " " + dose_number +"\n")                                        
    elif "ml" in info or "msl" in info or "milliliter" in info or "millilitre" in info:
     #   print line.strip()
        if regex_ml2:
            regex_triple = re.compile('([0-9])\s([0-9])\s([0-9])')
            regex_triple2 = re.search(regex_triple, info)
            if regex_triple2:
                quantity1 = int(convert(regex_triple2.group(1)))
                quantity2 = int(convert(regex_triple2.group(2)))
                dose_number_1 = quantity1 * int(regex_triple2.group(3))
                dose_number_2 = quantity2 * int(regex_triple2.group(3))
                if dose_number_1 > dose_number_2:
                    dose_number_max = dose_number_1
                    dose_number_min = dose_number_2
                    new_extracted_dose_number.write(text_id2 + " " + str(dose_number_min) + "-" + str(dose_number_max) +"\n")
                elif int(dose_number_1) == int(dose_number_2):
                    new_extracted_dose_number.write(text_id2 + " " + str(dose_number_min) + "-" + str(dose_number_max) +"\n")
                else:
                    new_extracted_dose_number.write(text_id2 + " " + str(dose_number_min) + "-" + str(dose_number_max) +"\n") 
            else:
                quantity = float(convert(regex_ml2.group(1)))
                dose_number = quantity * float(regex_ml2.group(2))
                dose_number = no_zero(dose_number)
                new_extracted_dose_number.write(text_id2+ " " +dose_number+"\n")            
        else:
            new_extracted_dose_number.write(text_id2+ " 1"+"\n")
    elif regex_latin2:
#        print line.strip()
        number1 = regex_latin2.group(1)
        number2 = regex_latin2.group(2)
        if float(number1) > float(number2):
            new_number1 = number2
            new_number2 = number1
            number1 = new_number1
            number2 = new_number2
            new_extracted_dose_number.write(text_id2 + " " + number1 + "-" + number2 +"\n")
        elif float(number1) == float(number2):
            new_extracted_dose_number.write(text_id2 + " " + number1 + "-" + number2 +"\n")                                     
        else:
            new_extracted_dose_number.write(text_id2 + " " + number1 + "-" + number2 +"\n") 
    elif regex_latin_single2:
      #  print line.strip()
        number1 = regex_latin_single2.group(1)
        new_extracted_dose_number.write(text_id2+ " " +number1+"\n")
    elif regex_other_day2:
     #   print line
        dose_number_min = regex_other_day2.group(1)
        dose_number_max = regex_other_day2.group(2)

        if float(dose_number_min) > float(dose_number_max):
            new_number1 = dose_number_max
            new_number2 = dose_number_min
            dose_number_min = new_number1
            dose_number_max = new_number2
            new_extracted_dose_number.write(text_id2 + " " + dose_number_min + "-" + dose_number_max +"\n")

        elif float(dose_number_min) == float(dose_number_max):
            new_extracted_dose_number.write(text_id2 + " " + dose_number_min + "-" + dose_number_max +"\n")
        else:
            new_extracted_dose_number.write(text_id2 + " " + dose_number_min + "-" + dose_number_max +"\n") 
    elif regex_two_periods2:
  #      print line
        dose_number_min = regex_two_periods2.group(1)
        dose_number_max = regex_two_periods2.group(2)
        dose_number = (float(dose_number_min) + float(dose_number_max))/2
        actual_dose_number = no_zero(dose_number)
        new_extracted_dose_number.write(text_id2 + " " + actual_dose_number + "-" + actual_dose_number +"\n")  
    elif "cap" in info or "sachet" in info or "puf" in info or "tab" in info or "dr" in info or "amp" in info or "vial" in info or "pill" in info or "spray" in info or "patch" in info or "inh" in info or "suppos" in info or "blister" in info or "ounce" in info or "lozenge" in info or "bolus" in info or "microgram" in info or "mcg" in info or "gram" in info or "milligram" in info or "mg" in info or "g" in info or "millilitre" in info or "pack" in info or "packet" in info or "pastille" in info:
   #     print line.strip()
        new_extracted_dose_number.write(text_id2 + " 1"+"\n")   
    else:
#        print line.strip() ****here we can do the comparison between the two dosages with each other
        dash = info.endswith('-')
        dot = info.endswith('.')
        if dash == True:
            info = info.strip('-')
            new_extracted_dose_number.write(text_id2+ " " +info+"\n")
        elif dot == True:
            info = info.strip('.')
            new_extracted_dose_number.write(text_id2+ " " +info+"\n")
        else:            
            new_extracted_dose_number.write(line)
new_extracted_dose_number.close()
