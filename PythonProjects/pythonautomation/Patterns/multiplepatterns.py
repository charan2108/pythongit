import re
heroRegex = re.compile(r'Batman| Spiderman| Superman')
mo1 = heroRegex.search('Batman and Spiderman and Superman')
print(mo1.group())
mo2 = heroRegex.search('Spiderman And Superman')
print(mo2.group())
mo3 = heroRegex.search('Superman And Spiderman')
print(mo3.group())


heroRegex = re.compile(r'Bike|Car|Mobile|pc')
mo =heroRegex.search('Mobile is at 3km')
print(mo.group())
print(mo.group(1))


# import re
# phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# mo = phoneNumberRegex.search('My number is 455-555-9999')
# print(mo.group(1))