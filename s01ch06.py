#!/usr/bin/env python3.6
import cryptopals
import base64
import itertools

def breakRepeatingXor(data, keySize):
    blocks = [ data[i:i+keySize] for i in range(0, len(data), keySize) ]
    transposedBlocks = list(itertools.zip_longest(*blocks, fillvalue=0))
    key = [(cryptopals.findXorKey(bytes(x))[0]) for x in transposedBlocks]
    return cryptopals.repeatingXor(data, bytes(key))

def averageNormalizedHammingDistance(data, keySize):
    blocks = [ data[i:i+keySize] for i in range(0, len(data), keySize) ][0:4]
    pairs = list(itertools.combinations(blocks, 2))
    scores = [ (cryptopals.getHammingDistance(p[0], p[1]) / float(keySize)) for p in pairs ][0:6]
    return sum(scores) / len(scores)

def predictKeySize(data, minSize=2, maxSize=40):
    #for i in range(minSize, maxSize + 1):
    for i in sorted(range(minSize, maxSize + 1), key=lambda k: averageNormalizedHammingDistance(data, k)):
        score = averageNormalizedHammingDistance(data, i)
        print('[%2d] Score = %f' % (i, score,))
    return min(range(minSize, maxSize + 1), key=lambda k: averageNormalizedHammingDistance(data, k))

input1 = "this is a test".encode('utf-8')
input2 = "wokka wokka!!!".encode('utf-8')
distance = cryptopals.getHammingDistance(input1, input2)

print('IN1: %s' % (input1,))
print('IN2: %s' % (input2,))
print('OUT: %d' % (distance,), end=' ')
cryptopals.test(distance, 37)

testStr = b'The possibility of a link between the earthquakes was being investigated in the days after the second one. Big earthquakes can increase the long-term risk of seismic activity by transferring "static stress" to adjacent faults, but only at a distance of up to four times the length of the original rupture. In the 19 September earthquake static stress transfer was considered unlikely due to the distance between the earthquakes, in excess of the expected 400 km maximum.'
testKey = b'alicia'
testOut = cryptopals.repeatingXor(testStr, testKey)
print('KEY: %d' % (predictKeySize(testOut),))
print('DEC: %s' % (breakRepeatingXor(testOut, 6),))

# read in 6.txt
with open('6.txt', 'r') as inFile:
    b64data = inFile.read()
    ciperdata = base64.b64decode(b64data)
