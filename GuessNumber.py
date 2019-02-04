#!/usr/bin/python 2.7

import os
import re
import random

KUO_ERROR = -1
NUM_LENGTH = 4

def stringtToCharacterArray( strNum ):
    charArray = []
    for i in strNum:
        charArray.append(i)

    while len(charArray) < NUM_LENGTH:
        charArray.insert(0, "0")

    return charArray

def checkNumber( checkNum ):
    if len(checkNum) != NUM_LENGTH:
        return False

    for k in range( NUM_LENGTH ):
        for j in range (k+1, NUM_LENGTH ):
            if checkNum[k] == checkNum[j]:
                return False

    return True

def numIsMatch( s1, s2 ):
    resultA = 0
    resultB = 0
    for k in range( NUM_LENGTH ):
        if s1[k] == s2[k]:
            resultA += 1

    for i in range( NUM_LENGTH ):
        for j in range( NUM_LENGTH ):
            if s1[i] == s2[j]:
                resultB += 1

    resultB -= resultA

    return (resultA, resultB)

def getNumTable():
    table = []
    for i in range( 0, 10**NUM_LENGTH ):
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
    tryNumber = ansList[0]

    while True:
        resList = []

        compResult = numIsMatch( questNum, tryNumber )

        tryCount+=1

        # print "Try", "".join(tryNumber), ". This is the", tryCount, "times tryed."
        # print "The result is", compResult[0], "A", compResult[1], "B"

        for compNum in ansList:
            res = numIsMatch( compNum, tryNumber )
            if (compResult[0] == res[0] and compResult[1] == res[1]):
                resList.append(compNum)

        ansList = resList

        if compResult[0] == NUM_LENGTH or len(ansList) == 0:
            break;

        tryNumber = ansList[random.randrange(len(ansList))]

    if len(ansList) != 1:
        print "Error! Can NOT find the answer"
    else:
        print "Total try", tryCount, "times, you entered number is", "".join(ansList[0])

    return tryCount

def guessNumberAlgorithm():
    cnt = 0
    count = 0
    total = 0
    ansTable = [0] * 9

    # count = guessNumber( stringtToCharacterArray(str(9876)) )
    # if count == KUO_ERROR:
    #     print "Unexpective Error occured! Applicaint were breaked!"
    #     break

    # break

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

    return

def checkResFmt( result ):
    if not re.compile("^\d[AB]\d[AB]$", re.IGNORECASE).match(result):
        print "Test break."
        return False

    try:
        A = int(result[0])
        B = int(result[2])
    except ValueError:
        return False

    if A+B > NUM_LENGTH:
        return False

    return True

tryCount = 0
ansList = getNumTable()
print "ansList len =", len(ansList)
tryNumber = ansList[random.randrange(len(ansList))]

while True:
    print "I guess the number is", "".join(tryNumber)

    while True:
        print "Enter the result"
        result = raw_input( "format:[XAXB](X: 0~" + str(NUM_LENGTH) + "):")
        if checkResFmt(result):
            break
        print "Format ERROR! Please check the format again."

    compResult = [int(result[0]), int(result[2])]

    resList = []

    tryCount+=1

    # print "Try", "".join(tryNumber), ". This is the", tryCount, "times tryed."
    # print "The result is", compResult[0], "A", compResult[1], "B"

    for compNum in ansList:
        res = numIsMatch( compNum, tryNumber )
        if (compResult[0] == res[0] and compResult[1] == res[1]):
            resList.append(compNum)

    ansList = resList
    print "ansList len =", len(ansList)

    if compResult[0] == NUM_LENGTH:
        print "Total try", tryCount, "times. The answer is", "".join(ansList[0])
        break
    elif len(ansList) == 1:
        print "The answer is", "".join(ansList[0]), ". Total try", tryCount+1, "times"
        break
    elif len(ansList) == 0:
        print "Error! Can NOT find the answer. You are cheating"
        break

    tryNumber = ansList[random.randrange(len(ansList))]

os.system("pause")
