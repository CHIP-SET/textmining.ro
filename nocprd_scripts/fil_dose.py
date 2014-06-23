#! usr/local/python

#date: 05/08/2011
#author: george karystianis
import sys

# this is a script that filters the minorthird output data and reduces the number of sub spans. takes as an iput the original minor third output and prodcued a filered one.
#por ejemplo, we have a span of interest: good-morning, my name is george. Let's say we have written rules that extract

# *********good-morning*********** (1)
# *********george*****************  (2)
#****my name is george********* (3)
#AND
#******good-morning, my name is george*******

#with this script we eliminate the (1),(2) and (3)


minorthird_filter = open(sys.argv[2],'w')        # file you will write the minorthird filtered results

last_line = ""

cat = [1,2,3,4]
cats = ["dose_number","dose_unit","dose_frequency","dose_interval"]
for animal in cat:
    line_number = 0
    if last_line != "":
        minorthird_filter.write(last_line)
        last_line = ""
    #last_line = ""
    last_start = ""
    last_length = -1
    print 
    print "-------------------------------------------------"
    print "Doing your", cats[animal-1], "in category", animal
    for line in open(sys.argv[1],'r'):              # file you will open which is the minorthird label file
        if line=="\n":
            continue
        line_id = line.split()[1]
        start = line.split()[2]
        length = line.split()[3]
        category = line.split()[-1]
        if category == cats[animal-1]:
         #   print category
          #  print line_id
            if line_id == line_number:
           #     print line_id, line_number
                end = int(start) + int(length)
                last_end = int(last_start) + int(last_length)
                if (int(start) >= int(last_start) and int(start) < int(last_end)) or (int(last_start) >= int(start) and int(last_start) < int(end)):
                    if (int(length) > int(last_length)):
                        last_length = length
                        last_start = start
                        last_line = line
                        continue
                    else:
                        continue
                else:
                    continue
            line_number = line_id 
            last_start = start
            last_length = length
          #  print last_line
            minorthird_filter.write(last_line )
            last_line = line
#print last_line    
if last_line != "":
    minorthird_filter.write(last_line)
minorthird_filter.close()

