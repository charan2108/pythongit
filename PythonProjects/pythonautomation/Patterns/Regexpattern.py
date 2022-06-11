# importing the re module
import re
# storing the re.com[ile in phonNumberRegex
phoneNumberRegex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')
# Storing the regexpattern named phoneNumberRegex.search
mo =phoneNumberRegex.search('My mobile no is 415-555-5555')
print("Found Mobile no is "+mo.group())