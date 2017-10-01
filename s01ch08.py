#!/usr/bin/env python3
import cryptopals
import itertools

cipherdata = cryptopals.loadHexFile('8.txt')
print('Loaded %d blocks for analysis.' % (len(cipherdata),))

scores = []
for i in range(len(cipherdata)):
    #print('%d: %d bytes' % (i, len(cipherdata[i]),))

    block = cipherdata[i]
    subblocks = [block[i:i+16] for i in range(0, len(block), 16)]
    pairs = list(itertools.combinations(subblocks, 2))
    #print('%d: pairs: %d' % (i, len(pairs),))
    score = 0
    for p in pairs:
        if p[0] == p[1]:
            score += 1
            print('%d: score: %d' % (i, score,))
    scores.append((i, score,))

foundCipherText = max(scores, key=lambda k: k[1])
print('Found: %s' % (foundCipherText,))
print('Ciphertext: %s' % (cipherdata[foundCipherText[0]],))
print('Plaintext: %s' % (cryptopals.decryptAESData(cipherdata[foundCipherText[0]], b'YELLOW SUBMARINE'),))
