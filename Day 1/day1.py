import os

def sum2ToTargetBrute(target):
    f = open("input.txt", "r")
    expenses = f.readlines()
    


    for num1 in expenses:
        for num2 in expenses:
            if (int(num1)+ int(num2) == target):
                print(num1 + " " + num2)
                return int(num1) * int(num2)

def sum2ToTargetHash(expenses, target):
    expenseMap = set()
    for i in range(0, len(expenses)):
        complement = target - expenses[i]
        if (complement in expenseMap):
            print(complement)
            print(expenses[i])
            return complement * expenses[i]
        else:
            expenseMap.add(expenses[i])



        
def sum3ToTargetHash(expenses, target):
    expenseMap = set()
    for i in range(0, len(expenses)):
        currTarget = target - expenses[i]
        for j in range(i+1, len(expenses)):
            complementJ = currTarget - expenses[j]
            if(complementJ in expenseMap):
                print(expenses[i])
                print(complementJ)
                print(expenses[j])
                return expenses[i] * complementJ * expenses[j]
            else:
                expenseMap.add(expenses[j])
                

def getListfromInput():
    f = open("input.txt", "r")
    lst = []
    for line in f:
        lst.append(int(line))
    return lst

def getHashfromInput():
    s = set(getListfromInput())
    return s
    

if __name__ =='__main__':
    expensesList = getListfromInput()
    #expensesHash = getHashfromInput()

    print(sum3ToTargetHash(expensesList, 2020))
