map = []
offset = 0
def shift(seq, n):
    a = n % len(seq)
    return seq[a:] + seq[:a]
    
for i in range(26):
    map.append([chr(num) for num in range (ord("A"), ord("Z") + 1)])
    map[offset] = shift(map[offset], offset)
    offset += 1

def getMessage(encrypt):
    stringToEncrypt = input(f"Please enter a message to {'encrypt' if encrypt else 'decrypt'}: ")
    return "".join(filter(str.isalpha, stringToEncrypt)).upper()

def getKey(message):
    validKey = False
    while not validKey:
        keyWord = input("Please enter a key: ")
        keyWord = "".join(filter(str.isalpha, keyWord)).upper()
        if len(keyWord) <= len(message):
            validKey = True
    key = ""
    while len(key) != len(message):
        if len(key) < len(message):
            key = key + keyWord
        elif len(key) > len(message):
            key = key[:len(message)]
    return key

def encrypt(message, key):
    encryptedMessage = []

    for letter in range(len(message)):
        encryptedMessage.append(map[ord(message[letter]) - 65][ord(key[letter]) - 65])
    return "".join(encryptedMessage)

def decrypt(ciphertext, key):
    decryptedMessage = []

    for letter in range(len(ciphertext)):
        decryptedMessage.append(chr(map[ord(key[letter]) - 65].index(ciphertext[letter]) + 65))
    return "".join(decryptedMessage)

