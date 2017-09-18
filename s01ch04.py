#!/usr/bin/env python3.6
import cryptopals

finalKey = None
finalScr = 0.0
finalOut = ''

with open('4.txt') as inFile:
    fileLines = inFile.read().split('\n')
    for l in fileLines:
        xorKey, xorScr, xorOut = cryptopals.findXorKey(bytes.fromhex(l))
        if xorScr > finalScr:
            finalKey = xorKey
            finalScr = xorScr
            finalOut = xorOut

finalOut = finalOut.decode('utf-8').strip() # stringify
print('KEY: %s' % (finalKey,))
print('SCR: %s' % (finalScr,))
print('XOR: %s' % (finalOut,), end=' ')
cryptopals.test(finalOut, "Now that the party is jumping")
