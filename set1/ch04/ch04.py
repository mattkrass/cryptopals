#!/usr/bin/env python3.6
from array import array

dictWords = []

def scoreString(s):
    score = 0
    strChunks = s.upper().split()
    for w in strChunks:
        if w in dictWords:
            print('Matched: %s' % w)
            score = score + 1
    if score > 0: print('Potential: %s' % s)
    return score

def findXorKey(encStr):
    finalResult = b''
    finalKey = ''
    highestScore = -1
    for c in range(0, 255):
        score = 0
        result = array('B')
        for i in encStr:
            r = (i ^ c)
            result.append(r)
        score = scoreString(str(result.tobytes()))
        if score > highestScore:
            highestScore = score
            finalResult = result.tobytes()
            finalKey = c
    return (finalKey, highestScore, finalResult,)

with open('dict.txt', 'r') as inFile:
    dictWords = inFile.read().split('\n')

finalResult = b''
finalKey = ''
highestScore = 0

with open('4.txt', 'r') as inFile:
    fileLines = inFile.read().split('\n')
    for l in fileLines:
        key,  score, result = findXorKey(bytes.fromhex(l))
        if score > highestScore:
            highestScore = score
            finalResult = result
            finalKey = key

print('Key: "%s" Score: %d Str: "%s"' % (finalKey, highestScore, finalResult,))

