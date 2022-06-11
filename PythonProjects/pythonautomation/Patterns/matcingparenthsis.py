import re
phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d -\d\d\d\d)')
mo = phoneNumberRegex.search('My mobile no is (555) 444-9999')
print(mo.group())
print(mo.group(1))
print(mo.group(2))