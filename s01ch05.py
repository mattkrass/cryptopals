#!/usr/bin/env python3.6
import cryptopals

input1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode('utf-8')
key = 'ICE'.encode('UTF-8')

output1 = cryptopals.repeatingXor(input1, key).hex()
output2 = cryptopals.repeatingXor(bytes.fromhex(output1), key)

print('INP: %s' % (input1,))
print('KEY: %s' % (key,))
print('OUT: %s' % (output1,), end=' ')
cryptopals.test(output1, '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')
print('OUT: %s' % (output2,), end=' ')
cryptopals.test(output2, input1)
