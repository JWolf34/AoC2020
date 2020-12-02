import os

def add2To2020():
    f = open("input.txt", "r")
    expenses = f.readlines()
    
    tup = []


    for num1 in expenses:
        for num2 in expenses:
            if (int(num1)+ int(num2) == 2020):
                tup.append(int(num1))
                tup.append(int(num2))
                break
            
    print(tup)
    print(tup[0] * tup[1])


if __name__ =='__main__':
    add2To2020()
