import sys
def KSA(key): #Key-Scheduling Algorithm
    k = list(range(256))
    j = 0
    for i in range(256):
        j = (j + k[i] + key[i % len(key)]) % 256
        k[i], k[j] = k[j], k[i] #swap
    return k

def PRGA(k): #Pseudo random generation algorithm
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + k[i]) % 256
        k[i], k[j] = k[j], k[i] #swap
        K=k[(k[i] + k[j]) % 256]
        yield K

def RC4(k,text):
    stream = PRGA(k)
    for char in text:
        cipher_b= ord(char) ^ next(stream) #XOR operation
        sys.stdout.write("%02X" % (cipher_b))
    print()

if __name__ == '__main__':
    key = 'Key'#input("Key: ")
    text = 'Plaintext'#input("Text: ")
    key = [ord(char) for char in key]
    k = KSA(key)
    RC4(k,text)
