# import re
# phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# mo = phoneNumberRegex.search('My number is 455-555-9999')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(0))

# areaCode = mo.groups()
# print(areaCode)
# mainNumber = mo.groups()
# print(areaCode)

import re
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumberRegex.search('The mobile number is  555-666-9999')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

# retrive at once
print(mo.groups())
areaCode = mo.groups()[0]
print(areaCode)
mainNumber = mo.groups()[1]
print(mainNumber)