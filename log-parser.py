'''
in_file = open("test_excerpt.log-20180308", "rt")
contents = in_file.read()
in_file.close()
print(contents)
'''

import re

lines = []

with open("test_excerpt.log-20180308", "rt") as in_file:
#in_file = open("test_excerpt.log-20180308", "rt")
#contents = in_file.read()
    for line in in_file:
        #email = re.search(r"from=<hazel@orbitbrokers.ca>", line)
        #print(email)
        lines.append(line)
    #if re.search(r"from=<Sadaf.Goodarzi@robinsonpharma.com>", lines[8]):
        #print("Found")
    #else:
        #print("Not Found")
    for each_line in lines:
        if re.search(r"from=<Sadaf.Goodarzi@robinsonpharma.com>", each_line):
            #separate = []
            #for each_value in each_line:
                #separate.append(each_value)
            #print(separate)
            separate = each_line.split()
            queue_id = separate[5]
            print(queue_id)
