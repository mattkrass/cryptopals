import base64
from array import array

def hexStringToBase64Bytes(hexString):
    return base64.b64encode(bytes.fromhex(hexString))

def hexStringToBase64String(hexString):
    return hexStringToBase64Bytes(hexString).decode('utf-8')

def xorByteStrings(bytesA, bytesB):
    result = array('B')
    for a, b in zip(bytesA, bytesB):
        result.append(a ^ b)
    return result.tobytes()

def xorHexStrings(hexA, hexB):
    return xorByteStrings(bytes.fromhex(hexA), bytes.fromhex(hexB)).hex()

def singleByteXor(bytesA, key):
    result = array('B')
    for i in bytesA:
        result.append(i ^ key)
    return result.tobytes()

def repeatingXor(bytesA, bytesK):
    keyLen = len(bytesK)
    result = array('B')
    for i in range(len(bytesA)):
        result.append(bytesA[i] ^ bytesK[(i % keyLen)])
    return result.tobytes()

def freqScore(s):
    freqMap = {
        'a': 0.08167,
        'b': 0.01492,
        'c': 0.02782,
        'd': 0.04253,
        'e': 0.12702,
        'f': 0.02228,
        'g': 0.02015,
        'h': 0.06094,
        'i': 0.06966,
        'j': 0.00153,
        'k': 0.00772,
        'l': 0.04025,
        'm': 0.02406,
        'n': 0.06749,
        'o': 0.07507,
        'p': 0.01929,
        'q': 0.00095,
        'r': 0.05987,
        's': 0.06327,
        't': 0.09056,
        'u': 0.02758,
        'v': 0.00978,
        'w': 0.02360,
        'x': 0.00150,
        'y': 0.01974,
        'z': 0.00074,
        ' ': 0.19181
    }

    score = 0.0
    for i in s.lower():
        if 32 > i and i != 10: # non-printable, scrub out
            return 0.0
        i = chr(i)
        if i in freqMap:
            score = score + freqMap[i]
    return score

def findXorKey(encStr):
    finalResult = b''
    finalKey = ''
    highestScore = -1
    for c in range(0, 127):
        score = 0
        result = singleByteXor(encStr, c)
        score = freqScore(result)
        print('key = %c, score = %f' % (c, score,))
        if score > highestScore:
            highestScore = score
            finalResult = result
            finalKey = c
    return (finalKey, highestScore, finalResult,)

def test(a, b):
    if a == b:
        print('\033[0;32m[ PASS! ]\033[0;0m')
    else:
        print('\033[1;31m[ FAIL! ]\033[0;0m')

def getHammingDistance(bytesA, bytesB):
    if len(bytesA) != len(bytesB): return -1
    distance = 0

    for i, j in zip(bytesA, bytesB):
        bits = i ^ j
        for k in range(8):
            if bits & 1: distance = distance + 1
            bits = bits >> 1;
    return distance

def predictKeySize(bytesA, minKeySize, maxKeySize):
    lowestDistance = 9.0
    keySize = 0
    for i in range(minKeySize, maxKeySize+1):
        chunkA = bytesA[0:i]
        chunkB = bytesA[i:2*i]
        chunkC = bytesA[2*i:3*i]
        chunkD = bytesA[3*i:4*i]
        if len(chunkA) != i: break
        if len(chunkB) != i: break
        if len(chunkC) != i: break
        if len(chunkD) != i: break
        distAB = (float)(getHammingDistance(chunkA, chunkB)) / i
        distCD = (float)(getHammingDistance(chunkC, chunkD)) / i
        distance = (distAB + distCD) / 2
        if 0 > distance: break
        print('key size %d scores %f' % (i, distance,))
        if distance < lowestDistance:
            print('new winning key size: %d' % (i,))
            lowestDistance = distance
            keySize = i
    return keySize

def breakRepeatingKeyXor(data, minKeySize=2, maxKeySize=40):
    keySize = 6#predictKeySize(data, minKeySize, maxKeySize)
    key = array('B')
    blockInterval = int(len(data) / keySize)
    print('l = %s, k = %s, i = %s' % (len(data), keySize, blockInterval,))
    for i in range(keySize):
        block = data[i::blockInterval]
        print('block size: %d (%d)' % (len(block), keySize,))
        keyByte, keyScore, keyResult = findXorKey(block)
        key.append(keyByte)
    return key.tobytes()
