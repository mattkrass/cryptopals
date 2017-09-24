#!/usr/bin/env python3.6
import cryptopals
import base64

input1 = "this is a test".encode('utf-8')
input2 = "wokka wokka!!!".encode('utf-8')
key = 'ICE'.encode('UTF-8')

distance = cryptopals.getHammingDistance(input1, input2)

print('IN1: %s' % (input1,))
print('IN2: %s' % (input2,))
print('OUT: %d' % (distance,), end=' ')
cryptopals.test(distance, 37)

testStr = b'this is a much longer string than we had before, it will encrypt better!'
# for i in range(12):
#     print('i = %02d, %s' % (i, testStr[i*6:(i+1)*6],))
# for j in range(6):
#     print('j = %02d, %s' % (j, testStr[j::6],))
testKey = b'alicia'
testOut = cryptopals.repeatingXor(testStr, testKey)
testDec = cryptopals.repeatingXor(testOut, testKey)
print('testOut = %s' % (testOut,))
print('testDec = %s' % (testDec,), end=' ')
cryptopals.test(testDec, testStr)
key = cryptopals.breakRepeatingKeyXor(testOut)
print('KEY: %s (%d)' % (key, len(key)))
# read in 6.txt
#with open('6.txt', 'r') as inFile:
#    b64data = inFile.read()
#    ciperdata = base64.b64decode(b64data)
#    key = cryptopals.breakRepeatingKeyXor(ciperdata, 2, 40)
#    print('KEY: %s' % (key,))
#    plaindata = cryptopals.repeatingXor(ciperdata, key)
#    print('TXT: %s' % (plaindata,))
