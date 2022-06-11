# # seconds = [1,2,3.5,6,7]
# # current = 1.100139445
# # seconds.append(current)
# # print(seconds)

# seconds = [1.2323442655, 1.4534345567, 1.023458894]
# current = 1.10001399445
# seconds.append(current)

# # remove items
# seconds = [1.2323442655, 1.4534345567, 1.023458894]
# print(seconds)
# seconds.remove(1.4534345567)
# print(seconds)
# # AccessItems
# serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
# # access the third item
# # print(serials[2])
# # Access multiple items
# serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
# print(serials[0])
# print(serials[2])
# print(serials[5])

# # append weekend to workdays
# workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# weekend = ["Sat", "Sun"]
# workdays.append("sat")
# print(workdays)

# # slicing 
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[0])
# print(letters[1])
# print(letters[2])
# print(letters[3])
# print(letters[4])
# print(letters[5])
# print(letters[6])
# print(letters[:3])
# print(letters[0:4])
# print(letters[0:5])
# print(letters[0:6])
# print(letters[1:2])
# print(letters[1:3])
# print(letters[1:4])
# print(letters[1:5])
# print(letters[1:6])

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[0:3])
# print(letters[4:])

# # conversion between datatypes
# # conversion of tuple to list
# marks = (100,200,300)
# print(marks)
# final_marks = list(marks)
# print(final_marks)
# # conversion of list to tuple
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters)
# alphabet = tuple(letters)
# print(alphabet)
# # list to string
# lists = ['h','e','l','l','o']
# print(lists[:3])
# finals_list = str.join("", lists)
# print(finals_list)

# letters = ['a', 'b', 'c', 'd']

data = {"a":[1,2,3], "b":[4,5,6], "c":[7,8,9]}
print(data['b'][2])