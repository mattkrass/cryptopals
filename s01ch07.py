#!/usr/bin/env python3
import cryptopals

plaintext = cryptopals.decryptAESDataECB(cryptopals.loadBase64File('7.txt'), b'YELLOW SUBMARINE')
print('plaintext = %s' % (plaintext.decode('utf-8'),))
