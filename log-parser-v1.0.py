"""
******************************************************************************************
 * Copyright (C) 2018 Fresa Technologies - All Rights Reserved
 *
 * Unauthorized copying of this file, via any medium is strictly  prohibited
 * Proprietary and confidential
 * Written by S. Iniyan <iniyan@fresatechnologies.com>, March - 2018

 The purpose of this program is to use the zimbra.log present at /var/log/ location
 and parse the log based on FROM EMAIL ID & QUEUE ID for the ease of analyzing.

 ***********************************    *******************************************************
"""


import re
import os

lines = []
temp_q_id = []
q_id = []
extract =[]

log_path = str(input("\n'Enter ABSOLUTE LOG path OR just LOG FILE NAME in case lOG FILE is present in SCRIPT FILE path'\nEnter zimbra log name: "))
email_id = input("\nEnter FROM email id: ")
query_id = "from=<"+email_id+">"
output_file = "excerpt.txt" # Output file for parsed log

if os.path.isfile(output_file):
    os.remove(output_file)

with open(log_path, 'rt') as input_file:
#with open(r"C:\Users\iniya\Desktop\T-Logs\zimbra.log-20180308", 'rt') as input_file:
    for line in input_file:
        lines.append(line)
    for each_line in lines:
        if re.search(query_id, each_line):
            separate = each_line.split()
            temp_q_id.append(separate[5].rstrip(':'))
    for each_element in temp_q_id:
        if each_element != "NOQUEUE" and each_element not in q_id:
            q_id.append(each_element)
    print(q_id)
    for element in q_id:
        for each_line in lines:
            if re.search(element, each_line) and each_line not in extract:
                extract.append(each_line)
                excerpt_file = open('excerpt.txt', 'a')
                excerpt_file.write(each_line)
                excerpt_file.close
