#!/usr/bin/env python3
import cryptopals

initial = b'YELLOW SUBMARINE' # 16 bytes
expected = b'YELLOW SUBMARINE\x04\x04\x04\x04' # 20 bytes

print('Initial  = %s' % (initial,))
print('Expected = %s' % (expected,), end=' ')
cryptopals.test(cryptopals.pcksPad(initial, 20), expected)

