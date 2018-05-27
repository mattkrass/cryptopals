#!/usr/bin/env python3
import cryptopals

key = b'YELLOW SUBMARINE'
initial = cryptopals.pcksPad(b'Loki the cat')
blockSize = 16
iv = bytes([ 0 ] * blockSize)
encryptedECB = cryptopals.encryptAESDataECB(initial, key)
encryptedCBC = cryptopals.encryptAESDataCBC(initial, key, iv)
decryptedECB = cryptopals.decryptAESDataECB(encryptedECB, key)
decryptedCBC = cryptopals.decryptAESDataCBC(encryptedCBC, key, iv)

print('Initial       = %s' % (initial,))
print('Encrypted ECB = %s' % (encryptedECB,))
print('Encrypted CBC = %s' % (encryptedCBC,), end=' ')
cryptopals.test(encryptedECB, encryptedCBC)
print('Decrypted ECB = %s' % (decryptedECB,), end = ' ')
cryptopals.test(decryptedECB, initial)
print('Decrypted CBC = %s' % (decryptedCBC,), end = ' ')
cryptopals.test(decryptedCBC, initial)

cipherdata = cryptopals.loadBase64File('10.txt')
plaindata = cryptopals.decryptAESDataCBC(cipherdata, key, iv)
print('plaindata = %s' % (plaindata.decode('utf-8'),))
