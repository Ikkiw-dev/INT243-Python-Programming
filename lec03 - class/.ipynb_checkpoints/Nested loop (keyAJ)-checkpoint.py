#Ex 1 : 4 rows of "O X O X"
def ex1():
    dim = range(4)

    for i in dim:
        for j in dim:
            if j % 2 != 0:
                print("X", end = " ")
            else:
                print("O", end = " ")
        print()
ex1()

def ex2():
    dim2 = range(5)
    for i in dim2:
        for j in dim2:
            print(j, end = " ")
        print()
ex2()

def ex3():
    RO = range(6) #row identifier
    RI = range(10, -1, -2) #column identifier
    for i in RO:
        for j in RI:
            print(j, end = " ")
        print()
ex3()