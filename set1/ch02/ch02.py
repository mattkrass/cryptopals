#!/usr/bin/env python3.6
from array import array

def fixedXor(buffer1, buffer2):
    if len(buffer1) != len(buffer2): return []
    result = array('B')
    for i, j in zip(buffer1, buffer2):
        result.append(i ^ j)
    return result.tobytes()

input1 = '1c0111001f010100061a024b53535009181c'
input2 = '686974207468652062756c6c277320657965'

bInput1 = bytes.fromhex(input1)
bInput2 = bytes.fromhex(input2)

bOutput1 = fixedXor(bInput1, bInput2)
print('bOutput1 = %s' % (bOutput1,))

