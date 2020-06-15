import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

random.randint(1,5)

def genEven():
    rdnum = random.randint(0,99)
    if (rdnum%2 == 1):
        rdnum -= 1
    return rdnum

def testGenEven(n = 10):
    result = []
    for i in range(n):
        result.append(genEven())
    print(result)

def deterministicNumber():
    rdnum = random.uniform(10,21)
    rdnum = int(rdnum)
    if (rdnum%2 == 1):
        rdnum -= 1
    return rdnum

def testDetNum(n = 10):
    result = []
    for i in range(n):
        result.append(deterministicNumber())
    numct = {}
    for i in result:
        if (i in numct):
            numct[i] += 1
        else:
            numct[i] = 1
    print(numct)