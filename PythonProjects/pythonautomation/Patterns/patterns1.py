def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for a in range(3):
        if not text[a].isdecimal():
            return False
        if text[3] != '-':
            return False
        for a in range(4,7):
            if not text[a].isdecimal():
                return False
        if text[7]!='-':
            return False
        for  a in range(8, 12):
            if not text[a].isdecimal(): 
                return False
    return True           
print('415-222-4242 is a mob number')
print(isPhoneNumber('415-222-4242'))

message ='Call me at 415-555-4242 Tommorrow. 415-555-9999 at office'
for a in range(len(message)):
    chunk = message[a:a+12]
    if isPhoneNumber(chunk):
        print("Phone Number is found "+ chunk)
print('Done')        
    