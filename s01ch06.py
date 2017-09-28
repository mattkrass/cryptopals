#!/usr/bin/env python3
import cryptopals

input1 = "this is a test".encode('utf-8')
input2 = "wokka wokka!!!".encode('utf-8')
distance = cryptopals.getHammingDistance(input1, input2)

print('IN1: %s' % (input1,))
print('IN2: %s' % (input2,))
print('OUT: %d' % (distance,), end=' ')
cryptopals.test(distance, 37)

cipherdata = cryptopals.loadBase64File('6.txt')
foundKey = cryptopals.breakRepeatingKeyXor(cipherdata)
print('KEY: %s' % (foundKey.decode('utf-8'),))
print('DEC: %s' % (cryptopals.repeatingXor(cipherdata, foundKey).decode('utf-8'),))
