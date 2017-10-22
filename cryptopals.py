import base64
import itertools
from array import array
from Cryptodome.Cipher import AES
import random

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
        i = chr(i)
        if i in freqMap:
            score += freqMap[i]
    return score

def findXorKey(encStr):
    finalResult = b''
    finalKey = ''
    highestScore = -1
    for c in range(0, 256):
        score = 0
        result = singleByteXor(encStr, c)
        score = freqScore(result)
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

def loadBase64File(filename):
    with open(filename, 'r') as inFile:
        return base64.b64decode(inFile.read())

def loadHexFile(filename):
    with open(filename, 'r') as inFile:
        return [bytes.fromhex(x) for x in inFile.read().split('\n')]

def getHammingDistance(bytesA, bytesB):
    if len(bytesA) != len(bytesB): return -1
    distance = 0

    for i, j in zip(bytesA, bytesB):
        bits = i ^ j
        for k in range(8):
            if bits & 1: distance = distance + 1
            bits = bits >> 1;
    return distance

def averageNormalizedHammingDistance(data, keySize):
    blocks = [ data[i:i+keySize] for i in range(0, len(data), keySize) ][0:4]
    pairs = list(itertools.combinations(blocks, 2))
    scores = [ (getHammingDistance(p[0], p[1]) / float(keySize)) for p in pairs ][0:6]
    return sum(scores) / len(scores)

def predictKeySize(data, minSize=2, maxSize=40):
    return min(range(minSize, maxSize + 1), key=lambda k: averageNormalizedHammingDistance(data, k))

def breakRepeatingKeyXor(data, minKeySize=2, maxKeySize=40):
    keySize = predictKeySize(data, minKeySize, maxKeySize)
    blocks = [ data[i:i+keySize] for i in range(0, len(data), keySize) ]
    transposedBlocks = list(itertools.zip_longest(*blocks, fillvalue=0))
    key = [(findXorKey(bytes(x))[0]) for x in transposedBlocks]
    return bytes(key)

def decryptAESDataECB(data, key):
    return AES.new(key, AES.MODE_ECB).decrypt(data)

def encryptAESDataECB(data, key, blockSize=16):
    if len(data) % blockSize != 0: # pad it out
        data = pcksPad(data, blockSize)
    return AES.new(key, AES.MODE_ECB).encrypt(data)

def pcksPad(data, blockSize=16):
    if blockSize > 255: raise Exception('blockSize must be able to fit in a byte!')
    padLength = blockSize - (len(data) % blockSize)
    return data + bytes([padLength] * padLength)

def encryptAESDataCBC(data, key, blockSize=16):
    aes = AES.new(key, AES.MODE_ECB)
    if len(data) % blockSize != 0: # pad it out
        data = pcksPad(data, blockSize)
    blocks = [data[i:i+blockSize] for i in range(0, len(data), blockSize)] 
    iv = bytes([ 0 ] * blockSize)
    result = b''
    for block in blocks:
        iv = aes.encrypt(xorByteStrings(block, iv))
        result += iv
    return result

def decryptAESDataCBC(data, key, blockSize=16):
    aes = AES.new(key, AES.MODE_ECB)
    blocks = [data[i:i+blockSize] for i in range(0, len(data), blockSize)] 
    iv = bytes([ 0 ] * blockSize)
    result = b''
    for block in blocks:
        result += xorByteStrings(aes.decrypt(block), iv)
        iv = block

    return result

def encryptionOracle(data):
    random.seed()
    key = bytes([random.randint(0, 255) for x in range(16)])
    print('Generated key = %s' % (key.hex(),))
    useECB = random.choice([True, False])

    aes = None
    if useECB:
        aes = AES.new(key, AES.MODE_ECB)
    else:
        aes = AES.new(key, AES.MODE_CBC)

    return data

if '__main__' == __name__:
    print('Module self-test!')
    encryptionOracle(b'')
