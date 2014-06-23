#!usr/local/python

import sys
import re

number_dict={"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "ten":"10", "apply":"1", "applied":"1","half":"0.5", "quarter":"0.25", "a":"1", "once":"1", "tablet":"1", "a half":"0.5", "eleven":"11","twelve":"12","thirteen":"13","fourteen":"14","fifteen":"15","sixteen":"16","seventeen":"17", "eighteen":"18","nineteen":"19","twenty":"20", "i":"1", "ii":"2", "iii":"3", "iv":"4","v":"5","vi":"6","vii":"7"}

new_extracted_dose_number = open(sys.argv[2], 'w')

def convert(n): #function that converts a word number into a number when it is called :P
    if n in number_dict:
        return number_dict[n]
    else:
        return n

def no_zero(n):
    if ".0" in str(n):
        n = str(int(n))
    else:
        n = str(round(n,1))
    return n

def double_dose(x, y, z):
    dose_number_1 = float(convert(x))
    dose_number_2 = float(convert(y))
    actual_dose = (dose_number_1+dose_number_2)/2
    actual_dose = no_zero(actual_dose)
    line = z + " " + str(actual_dose)
    return line

regex_ml = re.compile('(ml|mls|msl)')

regex_ml_x = re.compile('([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:x)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:ml|mls|msl|gms|gram|microgram|mcg|mg|milligram)')

regex_ml_or = re.compile('([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:-|to)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:x)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:ml|mls|msl|gms|gram|microgram|mcg|mg|milligram)')

regex_ml_x_double = re.compile('([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:x)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:x)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:ml|mls|msl|gms|gram|microgram|mcg|mg|milligram)')

regex_single_ml = re.compile('([0-9]+.?[0-9]+?|[a-z]+)(?:\s+)?(?:-)?(?:\s+)?(ml|mls|msl|gms|gram|microgram|mcg|mg|milligram)')

regex_ml_multiply = re.compile('([0-9]+|[a-z]+)(?:\s+)(?:to|or|-|/)(?:\s+)([0-9]+|[a-z]+)(?:\s+)([0-9]+)(?:ml|mls|msl|gms|gram|microgram|mcg|mg|milligram)')

regex_number_ml = re.compile('([0-9]+|[a-z]+)(?:\s+)([0-9]+)(?:\s+)?(?:-)?(?:\s+)?(?:ml|mls|msl|gms|gram|microgram|mcg|mg|milligram)')

regex_dio_ml = re.compile('([0-9]+|[a-z]+)(?:\s+)?(?:-|to|or|/)(?:\s+)?([0-9]+|[a-z]+)(?:\s+)?(?:ml|mls|msl|gms|gram|microgram|mcg|mg|milligram)')

regex_dio_ml_more = re.compile('([0-9]+|[a-z]+)(?:\s+)?(?:ml|mls|msl)(?:\s+)?(?:-|to|or|/)(?:\s+)?([0-9]+|[a-z]+)(?:\s+)?(?:ml|mls|msl|gms|gram|microgram|mcg|mg|milligram)') #original version had ml mls msl

regex3 = re.compile('^[0-9]+\s+?once')

regex5 = re.compile('^[0-9]+\s+?[a-z]+')

regex_time_unit_dose = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|eleven|ten|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|[0-9]+.[0-9]+)(?:\s+)(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|drops|drop|drps|drp|drs|dr|pastille|pastilles|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|unit|units|grams|gram|milligram|milligrams|mcg|mg|mgs|^g$|gs|millilitre|millilitres|packs|packets|pack|packet)')

regex_period = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|eleven|ten|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|[0-9]+.[0-9]+)(?:\s+)?(?:in|at|every|each|a|an|before|after|during|per|with)(?:\s+)?(?:the|a|an)?(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|eleven|ten|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|[0-9]+.[0-9]+)(?:\s+)?(?:in|at|every|each|a|an|before|after|during|per|with)(?:\s+)?(?:the)?(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)')

regex_period_double = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|eleven|ten|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|drops|drop|drps|drp|drs|dr|pastille|pastilles|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|unit|units|grams|gram|milligram|milligrams|mcg|mg|mgs|^g$|gs|millilitre|millilitres|packs|packets|pack|packet)?(?:\s+)?(?:in|at|every|each|a|an|before|after|during|per|with)(?:\s+)?(?:the|a|an)?(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)\s?(?:and)?(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|eleven|ten|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|[0-9]+.[0-9]+)')

regex_period_alt = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|eleven|ten|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(?:\s+)?(?:in|at|every|each|a|an|before|after|during|per|with)?(?:\s+)?(?:the|a|an)?(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime|am|pm)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|one|two|three|four|five|six|seven|eight|nine|eleven|ten|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|[0-9]+.[0-9]+)')

regex_period_single = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty|[0-9]+.[0-9]+)(?:\s+)?(?:in|at|every|each|a|an|before|after|during|per|with)?(?:\s+)?(?:the)?(?:\s+)s?(?:morn|morning|mor|^eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)')

regex_up_to = re.compile('(?:up)(?:\s+)?(?:to)(?:\s+)?([0-9]+|[a-z]+)')

regex_dose_unit = re.compile('([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:-|to|or)(?:\s+)?([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|pastille|pastilles|drops|drop|drps|drp|drs|dr|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|mcg|mg|mgs|^g$|gs|millilitre|millilitres|packs|packets|pack|packet|unit|units)')

regex_dose_unit_single = re.compile('([0-9]+.?|[0-9]+.[0-9]+)(?:\s+)?(?:-)?(?:\s+)?(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|pastille|pastilles|drops|drop|drps|drp|drs|dr|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|mcg|mg|mgs|g|gs|millil|packs|packets|pack|packet|unit|units)')
           
regex_dose_unit_double = re.compile('([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|pastille|pastilles|drops|drop|drps|drp|drs|dr|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|unit|units|milligram|milligrams|mcg|mg|mgs|g\Z|gs|ml|msl|millilitre|millilitres|packs|packets|pack|packet)(?:\s+)?(?:or|-|to)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+)(?:\s+)?(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|pastille|pastilles|drops|drop|drps|drp|drs|dr|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|mcg|mg|mgs|g\Z|gs|ml|msl|millilitre|millilitres|packs|packets|pack|packet|unit|units)')

regex_nospaces = re.compile('([0-9]+|[0-9]+.[0-9]+|[a-z]+|1\/2)(?:\s+)?(?:-|to|or|\/)(?:\s+)?([0-9]+|[0-9]+.[0-9]+|[a-z]+)')

regex_dose_unit_period = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)?(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|pastille|pastilles|drops|drop|drps|drp|drs|dr|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|unit|units|mcg|mg|mgs|^g$|gs|ml|msl|millilitre|millilitres|packs|packets|pack|packet)(?:\s+)?(?:each|every|a|an|in|at|per|before|after|during|with)(?:\s+)?(?:the|a|an)?(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)?(?:each|every|a|an|in|at|during|after|before|per|with)?(?:\s+)?(?:the|a|an)?(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)')

regex_dose_unit_ampm = re.compile('([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|pastille|pastilles|drops|drop|drps|drp|drs|dr|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|unit|units|mcg|mg|mgs|^g$|gs|ml|msl|millilitre|millilitres|packs|packets|pack|packet)(?:\s+)?(?:each|every|a|an|in|at|per|before|after|during|with)(?:\s+)?(?:[0-9]+)(?:\s+)?(?:am|pm)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:each|every|a|an|in|at|during|after|before|per)?(?:\s+)?(?:am|pm)?')

regex_period_am = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)(?:[0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)(?:am|pm)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)(?:[0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|seventeen|sixteen|eighteen|nineteen|twenty)(?:\s+)(?:am|pm)')

regex_dose_unit_period_info = re.compile('([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:cap|capsules|caps|capsule|sachet|sachets|puf|puffs|puff|tabs|tab|tablet|tablets|pastille|pastilles|drops|drop|drps|drp|drs|unit|units|dr|ampoule|ampoules|amps|amp|vial|vials|pill|pills|sprays|spray|patch|patches|inh|suppos|blister|blisters|ounce|oucnes|lozenge|lozenges|bolus|boluses|micrograms|mcgs|grams|gram|milligram|milligrams|mcg|mg|mgs|^g$|gs|ml|msl|millilitre|millilitres|packs|packets|pack|packet)(?:\s+)?(?:[a-z]+)(?:\s+)(?:[a-z]+)(?:\s+)(?:each|every|a|an|in|at|per|during|after|before|with)(?:\s+)?(?:the)?(?:\s+)?(?:morning|mor|morn|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:each|every|a|an|in|at|during|after|before|per|with)?')

regex_double_meal = re.compile('([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:[a-z]+)(?:\s+)?(?:main\smeal|meal|dinner|breakfast|lunch|supper|food|evening\smeal)(?:\s+)?(?:and)(?:\s+)?([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:[a-z]+)(?:\s+)?(?:main\smeal|meal|dinner|breakfast|lunch|supper|food|evening\smeal)')

regex_double_meal_complicated = re.compile('([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|twenty|[0-9])(?:\s+)?(?:times|time)(?:\s+)?(?:each|every|a|an|in|at|per|during|after|before|with)(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)(?:\s+)?(?:[a-z]+)(?:\s+)?(?:main\smeal|meal|dinner|breakfast|lunch|supper|food|evening\smeal)(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|[a-z]+)(?:\s+)?(?:each|every|a|an|in|at|per|during|after|before|with)(?:\s+)?(?:morn|morning|mor|eve|evening|afternoon|noon|teatime|tea\stime|bedtime|dinner\stime|midnight|midday|night|dusk|dawn|day|mane|nocte|noct|morne|dinnertime|lunchtime|lunch\stime)')

regex_then = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten)(?:\s+)?(?:then|morn|noct|immediately|stat|now|mane|mor|nocte|now|immediatly|today)(?:\s+)?(?:and)?\s?(?:then|nocte|mor|mane|morn|noct|immediately|stat)?(?:\s+)?(?:and)?(?:\s+)?([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten)(?:\s+)?')

regex_and = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|twenty)(?:\s+)?(?:and)(?:\s+)?([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|twenty)')

regex_half = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|twenty)(?:\s+)?(?:and\sa|&|&\sa)?(?:\s+)?(half)')

regex_number_half = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|twenty)(?:\s+)?(?:and\sa|and|&|&\sa)?(?:\s+)?(1\/2)')

regex_m = re.compile('([0-9]+|[0-9]+.[0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|twenty)(?:m)')

regex_every_timeunit = re.compile('(every|each)(?:\s+)([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|nineteen|twenty)(?:\s+)(hour|hours|hrs|hr|month|minute|minutes|min|day|days|week|weeks|wk|wks|month|months|year|years|midday|yrs|yr|nights|night)')

bizarre_number = re.compile('([0-9])(\/)(52|12)')

for line in open(sys.argv[1],'r'):
    if "amount\n"==line:
        break
    txt = line.find('.txt')
    txt_id = line[:txt+4].strip()
    info = line[txt+5:].strip()
    regex4 = re.search(regex3, info)
    regex6 = re.search(regex5, info)
    regex_ml_multiply2 = re.search(regex_ml_multiply, info)
    regex_ml2 = re.search(regex_ml, info)
    regex_number_ml2 = re.search(regex_number_ml, info)
    regex_dio_ml2 = re.search(regex_dio_ml,info)
    regex_dio_ml_more2 = re.search(regex_dio_ml_more, info)
    regex_single_ml2 = re.search(regex_single_ml, info)
    regex_ml_x2 = re.search(regex_ml_x, info)
    regex_up_to2 = re.search(regex_up_to, info)
    regex_dose_unit2 = re.search(regex_dose_unit, info)
    regex_dose_unit_double2 = re.search(regex_dose_unit_double, info)
    regex_dose_unit_single2 = re.search(regex_dose_unit_single,info)
    regex_period2 = re.search(regex_period, info)
    regex_nospaces2 = re.search(regex_nospaces, info)
    regex_period_single2 = re.search(regex_period_single, info)
    regex_dose_unit_period2 = re.search(regex_dose_unit_period, info)
    regex_dose_unit_period_info2 = re.search(regex_dose_unit_period_info, info)
    regex_double_meal2 = re.search(regex_double_meal, info)
    regex_then2 = re.search(regex_then, info)
    regex_period_double2 = re.search(regex_period_double, info)
    regex_and2 = re.search(regex_and, info)
    regex_half2 = re.search(regex_half, info)
    regex_m2 = re.search(regex_m, info)
    regex_dose_unit_ampm2 = re.search(regex_dose_unit_ampm, info)
    regex_period_alt2 = re.search(regex_period_alt, info)
    regex_period_am2 = re.search(regex_period_am, info)
    regex_ml_x_double2 = re.search(regex_ml_x_double, info)
    regex_number_half2 = re.search(regex_number_half, info)
    regex_double_meal_complicated2 = re.search(regex_double_meal_complicated, info)
    regex_ml_or2 = re.search(regex_ml_or, info)
    regex_every_timeunit2 = re.search(regex_every_timeunit, info)
    bizarre_number2 = re.search(bizarre_number, info)
    regex_time_unit_dose2 = re.search(regex_time_unit_dose, info)
    if regex4:
      #  print line.strip()
        find_the_once = info.find('once')
        number=info[:find_the_once]
        line = txt_id + " " + number
    elif regex_double_meal_complicated2:
       # print line.strip()    
        line = double_dose(regex_double_meal_complicated2.group(1), regex_double_meal_complicated2.group(2), txt_id)
    elif regex_double_meal2:
      #  print line.strip()
        line = double_dose(regex_double_meal2.group(1), regex_double_meal2.group(2), txt_id)
    elif regex_dose_unit_period_info2:
     #   print line.strip()
        line = double_dose(regex_dose_unit_period_info2.group(1), regex_dose_unit_period_info2.group(2), txt_id)
    elif regex_dose_unit_double2:
      #  print line.strip()
        dose_number_1 = regex_dose_unit_double2.group(1)
        dose_number_2 = regex_dose_unit_double2.group(2)
        line = txt_id + " " + str(dose_number_1) + " or " + str(dose_number_2)
    elif regex_dose_unit_period2:
       # print line.strip()
        line = double_dose(regex_dose_unit_period2.group(1),regex_dose_unit_period2.group(2),txt_id)
    elif regex_period2:
      #  print line.strip(), regex_period2.group(1), regex_period2.group(2)
        line = double_dose(regex_period2.group(1),regex_period2.group(2),txt_id)
    elif regex_period_double2:
      #  print line.strip(), regex_period_double2.group(1),regex_period_double2.group(2)
        line = double_dose(regex_period_double2.group(1),regex_period_double2.group(2),txt_id)
    elif regex_period_am2:
      #  print regex_period_am2.group(1), regex_period_am2.group(2)
        line = double_dose(regex_period_am2.group(1),regex_period_am2.group(2),txt_id)
    elif regex_period_alt2:
      #  print line.strip()
        line = double_dose(regex_period_alt2.group(1),regex_period_alt2.group(2),txt_id)
    elif regex_period_single2:
      #  print line.strip()
        actual_dose_number = convert(regex_period_single2.group(1))
        line = txt_id + " " + str(actual_dose_number)         
    elif regex_up_to2:
      #  print line.strip()
        actual_dose = float(convert(regex_up_to2.group(1)))
        actual_dose = no_zero(actual_dose)
        line = txt_id + " " + "1-"+ str(actual_dose)
    elif regex_ml_x_double2:
      #  print line.strip()
        dose_number = float(convert(regex_ml_x_double2.group(1)))
        small_ml_dose = float(convert(regex_ml_x_double2.group(2)))
        extra_ml_dose = float(convert(regex_ml_x_double2.group(3)))
        actual_dose = dose_number * small_ml_dose * extra_ml_dose
        actual_dose = no_zero(actual_dose)
        line = txt_id + " " + str(actual_dose_number)   
    elif regex_ml_x2:
#        print line.strip()
        if regex_ml_or2:
            dose_number_1 = float(convert(regex_ml_or2.group(1)))
            dose_number_2 = float(convert(regex_ml_or2.group(2)))
            small_ml_dose = float(convert(regex_ml_or2.group(3)))
            actual_dose_number_1 = dose_number_1 * small_ml_dose
            actual_dose_number_2 = dose_number_2 * small_ml_dose
            actual_dose_number_1 = no_zero(actual_dose_number_1)
            actual_dose_number_2 = no_zero(actual_dose_number_2)
            line = txt_id + " " + str(actual_dose_number_1) + "-" + str(actual_dose_number_2)                
        else:
            if regex_ml_x2.group(1) == "1/2":
                dose_number = float(0.5)
                small_ml_dose = float(convert(regex_ml_x2.group(2)))
                actual_dose = dose_number * small_ml_dose
                actual_dose = no_zero(actual_dose)
                line = txt_id + " " + str(actual_dose)   
            else:
            #    print line.strip()
                dose_number = float(convert(regex_ml_x2.group(1)))
                small_ml_dose = float(convert(regex_ml_x2.group(2)))
                actual_dose = dose_number * small_ml_dose
                actual_dose = no_zero(actual_dose)
                line = txt_id + " " + str(actual_dose)        
               # print line
    elif regex_ml_multiply2:
     #   print line.strip()
        dose_number_1 = float(convert(regex_ml_multiply2.group(1)))
        dose_number_2 = float(convert(regex_ml_multiply2.group(2)))
        small_ml_dose = float(convert(regex_ml_multiply2.group(3)))
        dose_number_min = dose_number_1 * small_ml_dose
        dose_number_max = dose_number_2 * small_ml_dose
        dose_number_min = no_zero(dose_number_min)
        dose_number_max = no_zero(dose_number_max)
        line = txt_id + " " + str(dose_number_min) + " or " + str(dose_number_max)
    elif regex_dio_ml_more2:
      #  print line.strip()
        dose_number_min = float(convert(regex_dio_ml_more2.group(1)))
        dose_number_max = float(convert(regex_dio_ml_more2.group(2)))
        dose_number_min = no_zero(dose_number_min)
        dose_number_max = no_zero(dose_number_max)
        line = txt_id + " " + str(dose_number_min) + " or " + str(dose_number_max)
    elif regex_dio_ml2:
      #  print line.strip()
        dose_number_min = float(convert(regex_dio_ml2.group(1)))
        dose_number_max = float(convert(regex_dio_ml2.group(2)))
        dose_number_min = no_zero(dose_number_min)
        dose_number_max = no_zero(dose_number_max)
        line = txt_id + " " + str(dose_number_min) + " or " + str(dose_number_max)
    elif regex_number_ml2:
    #    print line.strip()
        if "x" in info:
            if regex_number_ml2.group(1) == "x":
                dose_number = float(convert(regex_number_ml2.group(2)))
                dose_number = no_zero(dose_number)
                line = txt_id + " " + str(dose_number)
            else:
                dose_number = float(convert(regex_number_ml2.group(1)))
                small_ml_dose = float(convert(regex_number_ml2.group(2)))
                actual_dose_number = dose_number * small_ml_dose
                actual_dose_number = no_zero(actual_dose_number)
                line = txt_id + " " + str(actual_dose_number)
        else:
            dose_number = float(convert(regex_number_ml2.group(1)))
            small_ml_dose = float(convert(regex_number_ml2.group(2)))
            actual_dose_number = dose_number * small_ml_dose
            actual_dose_number = no_zero(actual_dose_number)
            line = txt_id + " " + str(actual_dose_number)
    elif regex_single_ml2:
       # print line.strip()
        dose_number = convert(regex_single_ml2.group(1))
        line = txt_id + " " + str(dose_number)
    elif regex_then2:
       # print line.strip()
        line = double_dose(regex_then2.group(1), regex_then2.group(2), txt_id)
    elif "half" in info:
      #  print line.strip()
        if regex_half2:
            dose_number = float(convert(regex_half2.group(1))) + float(convert(regex_half2.group(2)))
            line = txt_id + " " + str(dose_number)
        else:
            line = line
    elif regex_number_half2:
      #  print line.strip()
        dose_number = float(convert(regex_number_half2.group(1))) + float(0.5)
        line = txt_id + " " + str(dose_number)        
    elif regex_dose_unit2:
     #   print line.strip()
        number1 = regex_dose_unit2.group(1)
        number2 = regex_dose_unit2.group(2)
        if float(number1) > float(number2):
            new_number1 = number2
            new_number2 = number1
            number1 = new_number1
            number2 = new_number2
            line = txt_id + " " + str(number1) + " or " + str(number2)
        elif float(number1) == float(number2):
            line = txt_id + " " + str(number1) + " or " + str(number2)
        else:
            line = txt_id + " " + str(number1) + " or " + str(number2)
    elif regex_dose_unit_single2:
      #  print line.strip()
        if "mg" in info:
            number1 = regex_dose_unit_single2.group(1).strip('m') #+ "g"
            line = txt_id + " " + number1
        elif "mcg" in info:
            number1 = regex_dose_unit_single2.group(1) #+ "mcg"
            line = txt_id + " " + number1
        elif "gs" in info:
            number1 = regex_dose_unit_single2.group(1) 
            line = txt_id + " " + number1
        elif "gm" in info:
            number1 = regex_dose_unit_single2.group(1) 
            line = txt_id + " " + number1
        else:
            number1 = regex_dose_unit_single2.group(1) #+ "g"
            line = txt_id + " " + number1
    elif regex6:
      #  print line.strip()
        dose_number = re.compile('^[0-9]\s+?(or|to|\s)\s+?([0-9]|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)')
        dose_number2 = re.search(dose_number,info)
        if dose_number2:
            line = line
            if regex_nospaces2:
                number1 = convert(regex_nospaces2.group(1))
                number2 = convert(regex_nospaces2.group(2))
                if float(number1) > float(number2):
                    new_number1 = number2
                    new_number2 = number1
                    number1 = new_number1
                    number2 = new_number2
                    line = txt_id + " " + str(number1) + " or " + str(number2)
                elif float(number1) == float(number2):
                    line = txt_id + " " + str(number1) + " or " + str(number2)
                else:
                    line = txt_id + " " + str(number1) + " or " + str(number2) 
        else:
            dose_number_text = re.compile('^[0-9]+')
            dose_number_text2= re.search(dose_number_text,info)
            if dose_number_text2:
                dose_number_text3 = dose_number_text2.group().strip()
                line = txt_id + " " + dose_number_text3
    elif regex_nospaces2:
      #  print line.strip()
        half_regular_double = re.compile('([0-9]+)(?:\s+)?(?:\/)(?:\s+)?([0-9])(?:-|to|or)?(?:\s+)?([0-9]+)')
        half_regular_double2 = re.search(half_regular_double, info)
        half_regular = re.compile('([0-9]+)(?:\s+)?(?:\/)(?:\s+)?([0-9])')
        half_regular2 = re.search(half_regular, info)
        if half_regular_double2:
            number1 = float(half_regular_double2.group(1))/float(half_regular_double2.group(2))
            actual_dose = str(round(number1,1))
            number2 = convert(half_regular_double2.group(3))
            actual_dose2 = float(actual_dose) + float(number2)
            line = txt_id + " " + str(actual_dose2)
        elif bizarre_number2:
            line = txt_id + " ?"
        elif half_regular2:
            number1 = float(half_regular2.group(1))/float(half_regular2.group(2))
            actual_dose = str(round(number1,1))
            line = txt_id + " " + actual_dose
        else:
            number1 = convert(regex_nospaces2.group(1))
            number2 = convert(regex_nospaces2.group(2))
            if float(number1) > float(number2):
                new_number1 = number2
                new_number2 = number1
                number1 = new_number1
                number2 = new_number2
                line = txt_id + " " + str(number1) + " or " + str(number2)
            elif float(number1) == float(number2):
                line = txt_id + " " + str(number1) + " or " + str(number2)
            else:
                line = txt_id + " " + str(number1) + " or " + str(number2)   
    elif regex_and2:
       # print line.strip()     
        number1 = convert(regex_and2.group(1))
        number2 = convert(regex_and2.group(2))
        if float(number1) > float(number2):
            new_number1 = number2
            new_number2 = number1
            number1 = new_number1
            number2 = new_number2
            line = txt_id + " " + str(number1) + " or " + str(number2)
        elif float(number1) == float(number2):
            line = txt_id + " " + str(number1) + " or " + str(number2)
        else:
            line = txt_id + " " + str(number1) + " or " + str(number2)   
    elif "twice" ==info or "once" ==info or "thrice"==info:
       # print line.strip()
        line = txt_id + " ?" 
    elif regex_dose_unit_ampm2:
       # print line.strip()
        line = double_dose(regex_dose_unit_ampm2.group(1), regex_dose_unit_ampm2.group(2), txt_id)
    elif "dose" in info:
      #  print line.strip()
        boundary = info.find('dose')
        dose_number = info[:boundary].strip().strip('.')
        line = txt_id + " " + dose_number  
    elif "up to" in info:
    #    print line.strip()
        regex_upto = re.compile('(?:up\sto)\s+([0-9]+)')
        regex_upto2 = re.search(regex_upto, info)
        dose_number = regex_upto2.group(1)
        line = txt_id + "1-" + dose_number  
    elif regex_every_timeunit2:
   #     print line.strip()
        line = txt_id + " 1"
    elif regex_time_unit_dose2:
      #  print line.strip()
        dn = convert(regex_time_unit_dose2.group(1))
        line = txt_id + " " + str(dn)
    tokens = line.split()
    for i, word in enumerate(tokens):
        if word in number_dict:
            tokens[i] = number_dict[word]
    tokens2 = " ".join(tokens)
    new_extracted_dose_number.write(tokens2+"\n")
new_extracted_dose_number.close()
