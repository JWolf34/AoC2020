import os

def addTo2020():
    f = open("input.txt", "r")
    expenses = f.readlines()

    tup = tuple

    for num1 in expenses:
        for num2 in expenses:
            if (num1 + num2 == 2020):
                tup = (num1, num2)
            
    print(tup)
    print(tup[0] * tup[1])


if __name__ =='__main__':
    addTo2020()