#!/usr/bin/env python3
import cryptopals
import itertools
import base64

def breakRepeatingXor(data, keySize):
    blocks = [ data[i:i+keySize] for i in range(0, len(data), keySize) ]
    transposedBlocks = list(itertools.zip_longest(*blocks, fillvalue=0))
    key = [(cryptopals.findXorKey(bytes(x))[0]) for x in transposedBlocks]
    return cryptopals.repeatingXor(data, bytes(key))

input1 = "this is a test".encode('utf-8')
input2 = "wokka wokka!!!".encode('utf-8')
distance = cryptopals.getHammingDistance(input1, input2)

print('IN1: %s' % (input1,))
print('IN2: %s' % (input2,))
print('OUT: %d' % (distance,), end=' ')
cryptopals.test(distance, 37)

# read in 6.txt
with open('6.txt', 'r') as inFile:
    b64data = inFile.read()
    cipherdata = base64.b64decode(b64data)
    #keySize = cryptopals.predictKeySize(cipherdata)
    foundKey = cryptopals.breakRepeatingKeyXor(cipherdata)
    #print('KEY: %d' % (keySize,))
    #print('DEC: %s' % (breakRepeatingXor(cipherdata, keySize).decode('utf-8'),))
    print('KEY: %s' % (foundKey.decode('utf-8'),))
    print('DEC: %s' % (cryptopals.repeatingXor(cipherdata, foundKey).decode('utf-8'),))
