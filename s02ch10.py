#!/usr/bin/env python3
import cryptopals

key = b'YELLOW SUBMARINE'
initial = cryptopals.pcksPad(b'Alicia Brown')
encrypted = cryptopals.encryptAESDataECB(initial, key)
encryptedCBC = cryptopals.encryptAESDataCBC(initial, key)
decrypted = cryptopals.decryptAESDataECB(encrypted, key)
decryptedCBC = cryptopals.decryptAESDataCBC(encryptedCBC, key)

print('Initial       = %s' % (initial,))
print('Encrypted     = %s' % (encrypted,))
print('Encrypted CBC = %s' % (encryptedCBC,), end=' ')
cryptopals.test(encrypted, encryptedCBC)
print('Decrypted     = %s' % (decrypted,), end = ' ')
cryptopals.test(decrypted, initial)
print('Decrypted CBC = %s' % (decryptedCBC,), end = ' ')
cryptopals.test(decryptedCBC, initial)

cipherdata = cryptopals.loadBase64File('10.txt')
plaindata = cryptopals.decryptAESDataCBC(cipherdata, key)
print('plaindata = %s' % (plaindata.decode('utf-8'),))
