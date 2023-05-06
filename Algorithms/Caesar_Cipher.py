def encrypt(text, s):
    result = ""
    for i, _ in enumerate(text):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s-65) % 26 + 65)
        elif char == " ":
            result += " "
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


string = str(input("Input the plaintext message  : "))
print("Ciphertext message : " + encrypt(string, 3))
