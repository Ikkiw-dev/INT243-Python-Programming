list1 = [1, 2, 3] #list
list2 = (1, 2, 3) #tuple

list1[-1] = "three"
print(list1) #[1, 2, 'three']

# list2[-1] = "three"
# print(list2) : got error because tuple cannot change value or modify

#try with append
list1.append("4")
print(list1)

# list2.append("4")
# print(list2) : error -> 'tuple' object has no attribute 'append'

#try with pop
list1.pop()
print(list1)

# list2.pop()
# print(list2)

#solution = re-assign value
list2=(1,2)