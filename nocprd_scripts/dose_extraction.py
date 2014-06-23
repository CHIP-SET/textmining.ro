#! usr/bin/python

#author: george Karystianis#
#date: 31/10/2012
#this is a script that fetches the spans recognised from minorthird. You need to define the folder that contains your corpus****** 

import sys
import re

numberofspans = 0
spans = open(sys.argv[2],'w')

number_dict = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "ten":"10", "half":"0.5", "quarter":"0.25", "eleven":"11", "twelve":"12"}

def convert(n): #function that converts a word number into a number when it is called :P
    if n in number_dict:
        return number_dict[n]
    else:
        return n


cat = [1,2,3,4,5]
cats = ["dose_number","amount","dose_unit","dose_frequency","dose_interval"]  #these are the categories/span classes where rules were written for them in MT. These have to be the same with the rules that you have defined in minorthird
for animal in cat:
    print 
    print "-------------------------------------------------"
    print "Doing your", cats[animal-1], "in category", animal
    spans.write(cats[animal-1]+"\n")
    for line in open(sys.argv[1]):
        if line.split()[0]=="addToType":
          #  print line
            if line.split()[4] == cats[animal-1]:
                line_id = line.split()[1]
                numberofspans = numberofspans + 1
                drdoom= open(sys.argv[3]+line_id).read()	#open the folder containing the abstracts ****** sys.argv[3] is the corpus/train_set
                index = int(line.split()[2])		#split the line further so you have the token where the span starts
                index2 = int(line.split()[3])		#and split the line on the 4rth part to get the whole span
                galactus = drdoom[index:index+index2].replace("\n"," ")       #in drdoom which is the doc2 folder and the respective file name, find the indexes
                print line_id, " ", galactus
                regex_half_less = re.compile('(half)\s(?:or|to)\s([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)')
                regex_half_more = re.compile('(half)\s(?:and)\s([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)')
                regex_half_extra_more = re.compile('([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)\s(?:and)\s(half)')
                regex_quarter_half = re.compile('(?:quarter)\s(?:half)\s(?:or|to)\s([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)')
                regex_quarter = re.compile('quarter')
                regex_half_less2 = re.search(regex_half_less, galactus)
                regex_half_more2 = re.search(regex_half_more, galactus)
                regex_half_extra_more2 = re.search(regex_half_extra_more, galactus)
                regex_quarter_half2 = re.search(regex_quarter_half, galactus)
                regex_quarter2 = re.search(regex_quarter, galactus)
                if regex_half_less2:
                    first_part = convert(regex_half_less2.group(1))
                    second_part = convert(regex_half_less2.group(2))
                    galactus = first_part + " or " + second_part
                    spans.write(line_id+ " " + galactus+"\n")
                elif regex_half_more2:
                    first_part = convert(regex_half_more2.group(1))
                    second_part = convert(regex_half_more2.group(2))
                    galactus = float(first_part) + float(second_part)
                    spans.write(line_id+ " " + str(galactus)+"\n")
                elif regex_half_extra_more2:
                    first_part = convert(regex_half_extra_more2.group(1))
                    second_part = convert(regex_half_extra_more2.group(2))
                    galactus = float(first_part) + float(second_part)
                    spans.write(line_id+ " " + str(galactus)+"\n")
                elif regex_quarter_half2:
                    first_part = "0.125"
                    second_part = convert(regex_quarter_half2.group(1))
                    galactus = first_part + "or" + second_part
                    spans.write(line_id+ " " + str(galactus)+"\n")
                elif regex_quarter2:
                    first_part = convert(regex_quarter2.group())
                    first_part = galactus
                else:
                    spans.write(line_id+ " " + galactus+"\n")
                #    print line_id        + " " + str(galactus)
    print ""
    print "the total number of spans is: ",numberofspans, " :", cats[animal-1]                 #this shows you the total number of spans inside the produced label file from MT
spans.close()
