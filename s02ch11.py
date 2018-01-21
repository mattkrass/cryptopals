#!/usr/bin/env python3
import cryptopals

plaintext  = b'The wheels on the bus go round and round, round and round, round and round.'
ciphertext = cryptopals.encryptionOracle(plaintext)

print('Plain text  = %s' % (plaintext,))
print('Cipher text = %s' % (ciphertext.hex(),))
