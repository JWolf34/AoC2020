
def numValidPasswordsCount(passwords):
    numValid = 0
    for policy in passwords:
        minmax = policy[0].split("-")
        minimum, maximum = int(minmax[0]), int(minmax[1])
        character = policy[1]
        password = policy[2]

        if(password.count(character) >= minimum and password.count(character) <= maximum ):
            numValid+=1

    return numValid

def numValidPasswordsPos(passwords):
    numValid = 0
    for policy in passwords:
        minmax = policy[0].split("-")
        minpos, maxpos = int(minmax[0]), int(minmax[1])
        character = policy[1]
        password = policy[2]



        if((password[minpos-1] == character) != (password[maxpos-1] == character)):
            numValid+=1

    return numValid

def getPassFromInput():
    f = open("input.txt")
    passwords = []
    for line in f:
        (num, character, password) = line.split()
        passwords.append((num, character[0], password))
    return passwords

if __name__ == "__main__":

    passwords = getPassFromInput()

    #Part 1
    #print(numValidPasswordsCount(passwords)

    #Part 2
    print(numValidPasswordsPos(passwords))