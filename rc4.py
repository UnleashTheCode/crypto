import sys
def KSA(key):
    k = list(range(256))
    j = 0
    for i in range(256):
        j = (j + k[i] + key[i % len(key)]) % 256
        k[i], k[j] = k[j], k[i]
    return k

def PRGA(k):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + k[i]) % 256
        k[i], k[j] = k[j], k[i]
        K=k[(k[i] + k[j]) % 256]
        yield K

def RC4(k,text):
    stream = PRGA(k)
    for char in text:
        cipher_b= ord(char) ^ next(stream)
        sys.stdout.write("%02X" % (cipher_b))
    print()

if __name__ == '__main__':
    key = 'Key'#input("Key: ")
    text = 'Plaintext'#input("Text: ")
    key = [ord(char) for char in key]
    k = KSA(key)
    RC4(k,text)