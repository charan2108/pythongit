# a_list= [1,'hello', [1,2,3], True]
# print(a_list)
# print(a_list[1])
# print(a_list[1:4])

A = [1,'a']
B = [2, 1,'d']

A.extend(B)
print(A)

A.append(B)
print(A)

A.insert(B)
print(A)