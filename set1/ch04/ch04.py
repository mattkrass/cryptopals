#!/usr/bin/env python3.6
from array import array

def freqScore(s):
    freqMap = {
        'a': 0.08167,
        'b': 0.01492,
        'c': 0.02782,
        'd': 0.04253,
        'e': 0.12702,
        'f': 0.02228,
        'g': 0.02015,
        'h': 0.06094,
        'i': 0.06966,
        'j': 0.00153,
        'k': 0.00772,
        'l': 0.04025,
        'm': 0.02406,
        'n': 0.06749,
        'o': 0.07507,
        'p': 0.01929,
        'q': 0.00095,
        'r': 0.05987,
        's': 0.06327,
        't': 0.09056,
        'u': 0.02758,
        'v': 0.00978,
        'w': 0.02360,
        'x': 0.00150,
        'y': 0.01974,
        'z': 0.00074
    }

    score = 0.0
    for i in s.lower():
        if 32 > i and i != 10: # non-printable, scrub out
            return 0.0
        i = chr(i)
        if i in freqMap:
            score = score + freqMap[i]
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
        score = freqScore(result.tobytes())
        if score > highestScore:
            highestScore = score
            finalResult = result.tobytes()
            finalKey = c
    return (finalKey, highestScore, finalResult,)

finalResult = b''
finalKey = ''
highestScore = 0

with open('4.txt', 'r') as inFile:
    fileLines = inFile.read().split('\n')
    for l in fileLines:
        key,  score, result = findXorKey(bytes.fromhex(l))
        if score > highestScore:
            print('New high score %f beats %f: %s' % (score, highestScore, result,))
            highestScore = score
            finalResult = result
            finalKey = key

print('Key: "%s" Score: %d Str: "%s"' % (finalKey, highestScore, finalResult,))

