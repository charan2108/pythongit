l1 = [1,2,3]
l2 = ['A', 'B', 'C']

print("before extend", l1)
print("before extend", l2)
l1.extend(l2)
l2.extend(l1)
print("after extend", l1)
print("after extend", l2)