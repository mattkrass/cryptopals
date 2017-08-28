#!/usr/bin/env python3.6
import base64

hexString = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
hexBytes = bytes.fromhex(hexString)
print('HEX: %s' % (hexBytes,))
b64Bytes = base64.b64encode(hexBytes)
print('B64: %s' % (b64Bytes,))

