#!/usr/bin/python
import sys; sys.path.append('.\\modules\\')

KUO_ERROR = -1

guessNumLength = 4

def stringtToCharacterArray( strNum ):
    charArray = []
    for i in strNum:
        charArray.append(i)

    while len(charArray) < guessNumLength:
        charArray.insert(0, "0")

    return charArray

def checkNumber( checkNum ):
    if len(checkNum) != guessNumLength:
        return False

    for k in range( guessNumLength ):
        for j in range (k+1, guessNumLength ):
            if checkNum[k] == checkNum[j]:
                return False

    return True

def numIsMatch( s1, s2 ):
    resultA = 0
    resultB = 0
    for k in range( guessNumLength ):
        if s1[k] == s2[k]:
            resultA += 1

    for i in range( guessNumLength ):
        for j in range( guessNumLength ):
            if s1[i] == s2[j]:
                resultB += 1

    resultB -= resultA

    return (resultA, resultB)

def getNumTable():
    table = []
    for i in range( 123, 9877 ):
        charNumber = stringtToCharacterArray(str(i))
        if checkNumber(charNumber):
            table.append(charNumber)

    return table

def guessNumber( questNum ):
    tryCount = 0

    #questNum = raw_input("Please enter four number: ")

    while checkNumber(questNum) == False:
        inputNumber = raw_input("Please enter four number: ")
        questNum = stringtToCharacterArray(str(inputNumber))

    ansList = getNumTable()

    while True:
        tryNumber = ansList[0]
        resList = []

        compResult = numIsMatch( questNum, tryNumber )

        tryCount+=1

        # print "This is the", tryCount, "times tryed."
        # print "The result is", compResult[0], "A", compResult[1], "B"

        for compNum in ansList:
            res = numIsMatch( compNum, tryNumber )
            if (compResult[0] == res[0] and compResult[1] == res[1]):
                resList.append(compNum)

        ansList = resList

        if compResult[0] == guessNumLength or len(ansList) == 0:
            break;

    if len(ansList) != 1:
        print "Error! Can NOT find the answer"
    else:
        print "Total try", tryCount, "times, you entered number is", "".join(ansList[0])

    return tryCount

while True:
    cnt = 0
    count = 0
    total = 0
    ansTable = [0] * 9

    # count = guessNumber( 4579 )
    # if count == KUO_ERROR:
    #     print "Unexpective Error occured! Applicaint were breaked!"
    #     break

    numberTable = getNumTable()

    for value in numberTable:
        count = guessNumber(value)

        if count == KUO_ERROR:
            print "Unexpective Error occured! Applicaint were breaked!"
            break

        ansTable[count-1] += 1
        total += count

        # cnt += 1
        # if cnt >= 10:
        #     break

    for index in range(len(ansTable)):
        print index+1, "times has", ansTable[index], "results."
        count += ansTable[index]

    print "Tryed", count, "times."
    print "The average times is", float(total)/count, "times."

    break