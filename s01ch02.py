#!/usr/bin/env python3.6
import cryptopals

input1 = '1c0111001f010100061a024b53535009181c'
input2 = '686974207468652062756c6c277320657965'
xorOut = cryptopals.xorHexStrings(input1, input2)

print('IN1: %s' % (input1,))
print('IN2: %s' % (input2,))
print('XOR: %s' % (xorOut,), end=' ')
cryptopals.test(xorOut, '746865206b696420646f6e277420706c6179')
