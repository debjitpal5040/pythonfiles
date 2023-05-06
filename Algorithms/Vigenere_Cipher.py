table = [[None for j in range(65)] for i in range(65)]
for i in range(26):
    table[0][i] = chr(i+65)
for i in range(26, 52):
    table[0][i] = chr(i+71)
for i in range(52, 62):
    table[0][i] = chr(i-4)
table[0][62] = "."
table[0][63] = ","
table[0][64] = "?"
for i in range(1, 65):
    table[i] = table[i-1][1:]+table[i-1][:1]
message = input("Enter the message to encrypt : ")
key = input("Enter the key : ")


def position(x):
    if x == ".":
        return 62
    elif x == ",":
        return 63
    elif x == "?":
        return 64
    elif x.isupper():
        return ord(x)-65
    elif x.islower():
        return ord(x)-71
    elif x.isdigit():
        return ord(x)+4


def character(x):
    if x == 62:
        return "."
    elif x == 63:
        return ","
    elif x == 64:
        return "?"
    elif 0 <= x <= 25:
        return chr(x+65)
    elif 26 <= x <= 51:
        return chr(x+71)
    elif 52 <= x <= 61:
        return chr(x-4)


def encrypt(message, key):
    cipher = ""
    msg = len(message)
    k = len(key)
    if k < msg:
        key *= (msg // k)
        key += key[:msg % k]
    for i in range(msg):
        cipher += table[position(message[i])][position(key[i])]
    return cipher


def decrypt(cipher, key):
    message = ""
    msg = len(cipher)
    k = len(key)
    if k < msg:
        key *= (msg // k)
        key += key[:msg % k]
    for i in range(msg):
        column = table[position(key[i])].index(cipher[i])
        message += character(column)
    return message


ciphertext = encrypt(message, key)
print("Encrypted message :", ciphertext)
deciphertext = decrypt(ciphertext, key)
print("Decrypted message :", deciphertext)
