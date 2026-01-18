#variable declaration
var1 = '10'
convert = int(var1)
print(type(var1)) #research keywords to see data types
print(type(convert))

Var1 = 2
print(Var1)

res1 = 2*5-6+0//8**2-2
res2 = (2*5-6+0)//(8**2)-2
print(res1)
print(res2)

print(4 * "Hello")
print(type(4 * "Hello"))

v1 = 3
v2 = str(3)

list1 = [1, 2, 3]
list2 = ['four', 5.0, None] #list can contains mix data types

print(list1[2])
#wats to change items in the list
list2[0] = 'Zeros'
print(list2) #result : ['Zeros', 5.0, None]


#slide19 challenge
list1x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#start from -1, with the last items on the list
print(list1x[-8]) #12, -8 element from the end
print(list1x[-17]) #3, -17 element from the end, correspond index 2 from the start


print(list1x[5:]) #[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], start at index 5 and so on
print(list1x[:9]) #start from first to index before the val

print(list1x[0:9]) #[1, 2, 3, 4, 5, 6, 7, 8, 9], start at index 0 and stop before index 9

#change items in the list
list1x[9] = 'eight'
print(list1x) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 'eight', 11, 12, 13, 14, 15, 16, 17, 18, 19]
list1x[7:9] = ['five', 'six', 'ten']
print(list1x) #[1, 2, 3, 4, 5, 6, 7, 'five', 'six', 'ten', 'eight', 11, 12, 13, 14, 15, 16, 17, 18, 19]


#Extra : String Manipulation
text = "Hello My name is Bob." #feels like items in the list
print(text[0]) #H

#Extra : List Manipulation with the instance functions
listextra = ["one", "two", "three", "four"]
#append function : continue filling from the last one
listextra.append(5)
print(listextra) #['one', 'two', 'three', 'four', 5]
#insert function : insert where that you want (index required)
listextra.insert(1, "Hello")
print(listextra) #['one', 'Hello', 'two', 'three', 'four', 5]
#extend : add another list to the original list, an argument must be the list
listextra.extend([6, "seven"])
print(listextra) #['one', 'Hello', 'two', 'three', 'four', 5, 6, 'seven']

listextra.extend([None])
print(listextra)  #['one', 'Hello', 'two', 'three', 'four', 5, 6, 'seven', None]


#Removing the List
#remove function : remove specific items in a list -> value required, อ่านจากตัวเริ่มต้นไปท้าย ถ้าเจอซ้ำกัน 2 ตัว เอาตัวที่ index อยู่น้อยออกก่อน
listextra.remove(None)
print(listextra) #['one', 'Hello', 'two', 'three', 'four', 5, 6, 'seven']
listextra.remove("seven")
print(listextra) #['one', 'Hello', 'two', 'three', 'four', 5, 6]
#pop : remove the last items in a list
listextra.pop()
print(listextra) #['one', 'Hello', 'two', 'three', 'four', 5]
#clear : empty a list, remove all items in the list
listextra.clear()
print(listextra) #[]

#challenge on list manipulation
l1 = [1, 2, 3] + [4, 5, 6] #concatenate 2 list, extend the list การต่อ list
l2 = [0,1]*3 #repetition
l3 = ['1'] + ['3']
l4 = [1] + [4]

print(l1) #[1, 2, 3, 4, 5, 6]
print(l2) #[0, 1, 0, 1, 0, 1]
print(l3) #['1', '3']
print(l4) #[1, 4]

# print([1] + 3) -> error, differ data type
print([1] + ['2']) #[1, '2']

list3 = list(["one", "two", "three", "four"])
print(list3) #['one', 'two', 'three', 'four']

tuple1 = (1, 2, 3)
print(tuple1[0]) #1
print(tuple1[-1]) #3
