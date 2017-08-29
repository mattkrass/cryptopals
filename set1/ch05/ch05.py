#!/usr/bin/env python3.6
from array import array

def encryptWithRepeatingKey(key, s):
    keyLen = len(key)
    result = array('B')
    b = s.encode('ascii')
    k = key.encode('ascii')
    for i in range(len(b)):
        r = b[i] ^ k[i % keyLen]
        result.append(r)
    return result.tobytes()

inputString = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
cipherString = encryptWithRepeatingKey('ICE', inputString)
print(cipherString.hex())
decryptedString = encryptWithRepeatingKey('ICE', cipherString.decode('ascii'))
print(decryptedString.decode('ascii'))
