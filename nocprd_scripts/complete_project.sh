#!/bin/sh

source /var/odin/work/minorthird/script/setup.linux

cd /var/odin/work/minorthird

#java -Xmx2G edu.cmu.minorthird.ui.RunMixup -labels /var/odin/work/year\ 4/project/new_dosage_space/ -mixup /var/odin/work/year\ 4/project/nocprd_scripts/dose_characteristics.mixup -saveAs  /var/odin/work/year\ 4/project/nd_results/dosenumber50000.labels

java -Xmx2G edu.cmu.minorthird.ui.RunMixup -labels /var/odin/work/year\ 4/project/new_data/ -mixup /var/odin/work/year\ 4/project/nocprd_scripts/dose_characteristics.mixup -saveAs  /var/odin/work/year\ 4/project/nd_results/dosenumber50000.labels

cd ..
cd year\ 4/project 

####extracting the necessary spans####

bash  nocprd_scripts/blank_line.sh   nd_results/dosenumber50000.labels
#removing the blank line from the minorthird produced file

python  nocprd_scripts/fil_dose.py  nd_results/dosenumber50000.labels    nd_results/fil_dosenumber50000.labels
#filtering the minorthird spans - this gives the true number of filtered spans

python  nocprd_scripts/dose_extraction.py  nd_results/fil_dosenumber50000.labels   nd_results/extracted_medinfo50000.txt new_data/
#extract the dose number from the text

python  nocprd_scripts/word_digit_con.py  nd_results/extracted_medinfo50000.txt   nd_results/converted_dose_numbers50000.txt
#convert the number from the extracted dose numbers - if they are string, we convert them through a dictionary into numbers

python  nocprd_scripts/word_digit_con2.py  nd_results/converted_dose_numbers50000.txt   nd_results/new_converted_dose_numbers50000.txt
# here we convert the extra 5-50000 ml that have been appearing lately through the rule of the regular expressions - more dose numbers equal as 1 now.

python  nocprd_scripts/get_project_text.py   nd_results/new_converted_dose_numbers50000.txt    nd_results/new_converted_dose_numbers500002.txt

python  nocprd_scripts/column_comparison2.py  nd_results/new_converted_dose_numbers500002.txt  new_data2.txt   nd_results/50000columns.txt   #<------------------put original txt dosage file here
#here we add the dose number column and taken the text from the original source file of cprd data

python  nocprd_scripts/required.py  nd_results/extracted_medinfo50000.txt  nd_results/50000columns.txt   nd_results/new_50000columns.txt
# here we integrate the field "if it is required/needed

python  nocprd_scripts/add_dose_unit.py  nd_results/extracted_medinfo50000.txt  nd_results/new_50000columns.txt   nd_results/new_50000columns_units.txt
# here we integrate the following: we add the extracted dosage unit from us 

python nocprd_scripts/add_choice_of_dose.py  common_dosages.txt   nd_results/choice_of_dose50000.txt #new_compared_units_DNS50000.txt
#this should be the comparison between these two columns :P

python  nocprd_scripts/choice_dose_addition.py  nd_results/choice_of_dose50000.txt  nd_results/new_50000columns_units.txt    nd_results/all_columns_together50000.txt
#here we are adding the comparison of the choice of dose along with the other thus the all-collumns-together.

python  nocprd_scripts/freq_word_con.py  nd_results/extracted_medinfo50000.txt   nd_results/converted_frequency_numbers50000.txt
#Hconvert the word frequencies into number - that is probably the toughest of everything :P - probably needs more work when we work with the 1,000 set.

python  nocprd_scripts/get_project_text_frequency.py   nd_results/converted_frequency_numbers50000.txt    nd_results/converted_frequency_numbers500002.txt

echo "adding here the dose frequency"

python  nocprd_scripts/add_dose_frequency.py  nd_results/converted_frequency_numbers500002.txt  common_dosages.txt   nd_results/columns_and_frequency50000.txt
# this will add the extracted dose frequencies along with the extracted dose numbers :P

python  nocprd_scripts/add_columns_frequency.py  nd_results/columns_and_frequency50000.txt   nd_results/all_columns_together50000.txt   nd_results/all_columns_together50000_fr.txt
#here we are adding together the columns of dose frequency coming from the columsn_and_frequency[number] with the rest of the related information of all_columns_together. :P

python  nocprd_scripts/required_conv.py  nd_results/all_columns_together50000_fr.txt   nd_results/all_columns_together50000_fr_conv.txt
#here we include zero in the dose frequency if it says that it is when required/needed/etc

python  nocprd_scripts/default_dose_number.py  nd_results/all_columns_together50000_fr_conv.txt   nd_results/default_dose_number50000.txt   nd_results/new_default_dose_number50000.txt
# here we converted the zeros into ? for anything i.e., dose number and dose frequency. also defaulting dose number into 1 if there is a frequency or verbs into the sentence.

echo "just before the end"

python  nocprd_scripts/conv_dose_interval.py  nd_results/extracted_medinfo50000.txt   nd_results/converted_dose_intervals50000.txt
#here we are converting the extracted text of dose intervals to 1, 2, 3, 4, .... etc :P

python  nocprd_scripts/add_dose_interval.py  nd_results/converted_dose_intervals50000.txt   nd_results/new_default_dose_number50000.txt   nd_results/all_columns_together50000_di_conv.txt
# here at the end we are adding the last column of dose interval in the final file! end of story! needs to try this in the 50000 lines!
