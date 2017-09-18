#!/usr/bin/env python3.6
import cryptopals

input1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
xorKey, xorScr, xorOut = cryptopals.findXorKey(bytes.fromhex(input1))
xorOut = xorOut.decode('utf-8') # convert to a str
print('KEY: %s' % (xorKey,))
print('SCR: %s' % (xorScr,))
print('XOR: %s' % (xorOut,), end=' ')
cryptopals.test(xorOut, "Cooking MC's like a pound of bacon")
