# RSA
from math import gcd
while True:
    choice = int(input("Enter 0 to encrypt or 1 to decrypt or 2 to exit : "))
    if choice == 0:
        message = int(input("Enter message to encrypt : "))
        p = int(input("Enter p : "))
        q = int(input("Enter q : "))
        n = p * q
        e = int(input("Enter e : "))
        phi = (p - 1) * (q - 1)
        k = 2
        while k < phi:
            if gcd(k, phi) == 1 and (k * phi + 1) % e == 0:
                break
            k += 1
        d = (k * phi + 1) // e
        encryption = pow(message, e, n)
        print("Encrypted message :", encryption)
    elif choice == 1:
        message = int(input("Enter the message to decrypt : "))
        decryption = pow(message, d, n)
        print("Decrypted message :", decryption)
    elif choice == 2:
        break
    else:
        print("Invalid choice")