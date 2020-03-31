
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
        yield k[(k[i] + k[j]) % 256]

def RC4(k,text):
    stream = PRGA(k)
    result = ''
    for char in text:
        byte = ord(char)
        cipher_b= byte ^ next(stream)
        result += result + chr(cipher_b)
    print (result)

if __name__ == '__main__':
    key = input("Key: ")
    text = input("Text: ")
    key = [ord(char) for char in key]
    k = KSA(key)
    RC4(k,text)