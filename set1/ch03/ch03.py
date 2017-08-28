#!/usr/bin/env python3.6
from array import array
def isPlaintextChar(c):
    if 65 <= c and 90 >= c: return True
    elif 97 <= c and 122 >= c: return True
    elif 32 == c: return True
    return False

def findXorKey(encStr):
    finalResult = b''
    finalKey = None
    highestScore = 0
    for c in range(0, 127):
        score = 0
        result = array('B')
        for i in encStr:
            r = (i ^ c)
            if (isPlaintextChar(r)): score = score + 1
            result.append(i ^ c)
        if score > highestScore:
            highestScore = score
            finalResult = result
            finalKey = c
    print('Key: "%c" Score: %d Str: "%s"' % (finalKey, highestScore, str(finalResult.tobytes(), 'utf-8'),))

findXorKey(bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))
