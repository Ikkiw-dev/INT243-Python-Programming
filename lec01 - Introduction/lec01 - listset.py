list1 = [1, 2, 3]
set1 = {1, 2, 3}
set2 = {4, 5, 6}

# print(set1 + set2) -> error
#solution to concatenate
print(set1.union(set2)) #{1, 2, 3, 4, 5, 6}
print(set1.intersection(set2)) #set()
print(set1.difference(set2)) #{1, 2, 3}

print(set1 - set2) #subtraction : {1, 2, 3}

