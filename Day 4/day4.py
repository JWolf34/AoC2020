



def numValidPassports(passports):
    numValidPassports = 0

    for passport in passports:
        print(passport)
        if (len(passport.keys()) < 7):
            pass
        elif (len(passport.keys()) == 7):
            numValidPassports += 1

    

def getPassports():
    f = open("input.txt", 'r')
    raw = f.read().split('\n\n')
    for i in range(0, len(raw)):
        raw[i] = raw[i].replace('\n', ' ')

    passports = [{}]* len(raw)

    for i in range(0, len(raw)):
        pairs = raw[i].split()
        for pair in pairs:
            pair = pair.split(':')
            key, value = pair[0], pair[1]
            passports[i][key] = value
        
    return passports

if __name__ =="__main__":
    passports = getPassports()
    #print(passports)
    
    #print(numValidPassports(passports))
