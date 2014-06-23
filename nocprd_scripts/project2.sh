#!/bin/sh

#source /var/odin/work/minorthird/script/setup.linux

#cd ..
#java -Xmx2G edu.cmu.minorthird.ui.RunMixup -labels /var/odin/year\ /4/project/dosage_space/ -mixup /var/odin/year\ /4/project/dose_characteristics.mixup -saveAs /var/odin/year\ /4/project/dosenumber50000.labels
#cd project 

#extracting the necessary spans

#bash blank_line.sh dosenumber50000.labels

#removing the blank line from the minorthird produced file

#python fil_dose.py dosenumber50000.labels  fil_dosenumber50000.labels

#filtering the minorthird spans - this gives the true number of filtered spans

#python dose_extraction.py fil_dosenumber50000.labels extracted_medinfo50000.txt ../var/odin/year\ /4/project/dosage_space/

#extract the dose number from the text

#python word_digit_con.py extracted_medinfo50000.txt converted_dose_numbers50000.txt

#convert the number from the extracted dose numbers - if they are string, we convert them through a dictionary into numbers

#python word_digit_con2.py converted_dose_numbers50000.txt new_converted_dose_numbers50000.txt

# here we convert the extra 5-6 ml that have been appearing lately through the rule of the regular expressions - more dose numbers equal as 1 now.

#python get_project_text.py  new_converted_dose_numbers50000.txt  new_converted_dose_numbers500002.txt

#python column_comparison2.py new_converted_dose_numbers500002.txt 50000.txt 50000columns.txt zero_file50000.txt disagreement_file50000.txt nothing_to_extract_file50000.txt

#here we do a comparison between the original file with "" or the CPRD and the one we are going to produce. Final outcome - text_id, text, extracted DN, CPRD dose number, symbol

#python add_amount_column2.py extracted_medinfo50000.txt 50000columns.txt new_50000columns.txt

# here we integrate the following: the ml amount as well as the field "if it is required/needed": text_id, text, extracted DN, CPRD dose number,amount,required, symbol

#python add_dose_unit.py extracted_medinfo50000.txt new_50000columns.txt new_50000columns_units.txt

# here we integrate the following: we add the extracted dosage unit from us 

python dose_unit_comp.py 50000.txt new_50000columns_units.txt new_compared_units_DNS50000.txt zero_file_dose_unit50000.txt disagreement_file50000_dose_unit.txt nothing_to_extract_file50000_dose_unit.txt

#we add the CPRD dosage unit and make comps. plus an extra symbol to see which one is different. Not sure if this is needed.

python add_choice_of_dose.py 50000.txt choice_of_dose50000.txt #new_compared_units_DNS50000.txt

#this should be the comparison between these two columns :P

python choice_of_dose_comp.py 50000.txt choice_of_dose50000.txt new_file_choice50000.txt zero_choice50000.txt disagreement50000_choice.txt nothing_to_extract_choice50000.txt

#python add the column of choice into the new_compared_units_DNS50000.txt - look below

python choice_dose_addition.py new_file_choice50000.txt new_compared_units_DNS50000.txt  all_columns_together50000.txt

#here we are adding the comparison of the choice of dose along with the other thus the all-collumns-together.

python freq_word_con.py extracted_medinfo50000.txt converted_frequency_numbers50000.txt

#Hconvert the word frequencies into number - that is probably the toughest of everything :P - probably needs more work when we work with the 1,000 set.

python get_project_text_frequency.py  converted_frequency_numbers50000.txt  converted_frequency_numbers500002.txt

python add_dose_frequency.py converted_frequency_numbers500002.txt 50000.txt columns_and_frequency50000.txt zero_frequency50000.txt disagreement_frequency50000.txt nothing_to_extract_frequency50000.txt 

# this will add the extracted dose frequencies along with the extracted dose numbers :P

python add_columns_frequency.py columns_and_frequency50000.txt all_columns_together50000.txt all_columns_together50000_fr.txt

#here we are adding together the columns of dose frequency coming from the columsn_and_frequency[number] with the rest of the related information of all_columns_together. :P

python required_conv.py all_columns_together50000_fr.txt all_columns_together50000_fr_conv.txt

#here we include zero in the dose frequency if it says that it is when required/needed/etc

python default_dose_number.py all_columns_together50000_fr_conv.txt default_dose_number50000.txt new_default_dose_number50000.txt

# here we converted the zeros into ? for anything i.e., dose number and dose frequency. also defaulting dose number into 1 if there is a frequency or verbs into the sentence.

python conv_dose_interval.py extracted_medinfo50000.txt converted_dose_intervals50000.txt

#here we are converting the extracted text of dose intervals to 1, 2, 3, 4, .... etc :P

python add_dose_interval.py converted_dose_intervals50000.txt new_default_dose_number50000.txt all_columns_together50000_di_conv.txt

# here at the end we are adding the last column of dose interval in the final file! end of story! needs to try this in the 50000 lines!


