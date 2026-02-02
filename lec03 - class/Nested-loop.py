lst3 = []
i = 1

while i < 4:
    j = 1
    row = []
    while j < 4:
        row.append(f"{i}-{j}")
        j +=1

    lst3.append(row)
    i +=1

print(lst3)

#Exercise 1 - 4rows of "O X O X"
for i in range(4):
    for j in range(4):
        if j % 2 == 0:
            print("O", end = " ")
        else:
            print("X", end = " ")
    print()
#Exercise 2 : 5 rows of "1 2 3 4 5"
for x in range(5):
    for y in range(1,6):
        print(y, end = " ")
    print()

#Exercise 3 : 6 rows of "10 8 6 4 2 0"
for a in range(6):
    for b in range(10, -1, -2):
        print(b, end = " ")
    print()