# -*- coding: utf-8 -*-

import re


# pattern = "Cookie"
# sequence = "Cookie"
# if re.match(pattern, sequence):
#   print("Match!")
# else: print("Not a match!")

# line = "Cats are smarter than dogs and monkeys"

# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

# if matchObj:
#   print("matchObj.group() : ", matchObj.group())
#   print("matchObj.group(1) : ", matchObj.group(1))
#   print("matchObj.group(2) : ", matchObj.group(2))
  
# else:
#   print("No match!!")


'''
line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print("search --> searchObj.group() : ", searchObj.group())
else:
   print("Nothing found!!")
'''


#phone = "2004-959-559 # This is Phone Number"
#
## Delete Python-style comments
#num = re.sub(r'#.*', "", phone)
#print("Phone Num : ", num)
#
## Remove anything other than digits
#num = re.sub(r'\D', "", phone)    
#print("Phone Num : ",  num)

  


#regex = r"[a-zA-Z]+ \d+"
#matches = re.findall(regex, "June 24, August 9, Dec 12")
#for match in matches:
#   
#    print("Full match: %s" % (match))


'''
regex = r"([a-zA-Z]+)"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
   
    print("Match month: %s" % (match))
'''



regex = r"[a-zA-Z]+ \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
   
    print("Match at index: %s, %s" % (match.start(), match.end()))
