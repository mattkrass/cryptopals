#!/usr/bin/env python3.6
from array import array
import base64

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

def hamming(a, b):
    if len(a) != len(b): return -1
    if isinstance(a, str): a = a.encode('utf-8')
    if isinstance(b, str): b = b.encode('utf-8')
    if not isinstance(a, bytes): return -2
    if not isinstance(b, bytes): return -3
    distance = 0

    for i, j in zip(a, b):
        bits = i ^ j
        for k in range(8):
            if bits & 1: distance = distance + 1
            bits = bits >> 1
    return distance

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
    return finalKey

def encryptWithRepeatingKey(key, s):
    keyLen = len(key)
    result = array('B')
    for i in range(len(s)):
        r = s[i] ^ key[i % keyLen]
        result.append(r)
    return result.tobytes()

def breakRepeatingXorCypher(cyphertext, minKeySize=2, maxKeySize=40):
    lowestDistance = (maxKeySize * 8) + 1 # the distance must be lower than this for any possible chunk 
    probableKeySize = 0
    for keySize in range(minKeySize, maxKeySize+1):
        firstChunk = cyphertext[0:keySize]
        secondChunk = cyphertext[keySize:2*keySize]
        dist = hamming(firstChunk, secondChunk)
        print('keySize %d = %d' % (keySize, dist,))
        if dist < lowestDistance:
            probableKeySize = keySize
            lowestDistance = dist

    # partition the data based on probableKeySize
    key = array('B')
    for i in range(probableKeySize):
        key.append(findXorKey(cyphertext[i:probableKeySize:]))
    return key.tobytes()

binData = b''
with open('6.txt', 'r') as inFile:
    binData = base64.b64decode(inFile.read())

print('Got %d bytes decoded.' % (len(binData),))
key = breakRepeatingXorCypher(binData)
print('Got key = %s' % (key,))
print('%s' % (encryptWithRepeatingKey(key, binData),))

