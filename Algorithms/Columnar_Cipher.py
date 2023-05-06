# Columnar Transposition
from math import ceil
msg = input("Enter message to encrypt : ")
key = input("Enter key : ")


def encryptMessage(msg):
    cipher = ""
    msg_len = len(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = ceil(msg_len / col)
    fill_null = (row * col) - msg_len
    msg_lst = list(msg)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]
    k_indx = 0
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1
    return cipher


def decryptMessage(cipher):
    msg = ""
    msg_len = len(cipher)
    col = len(key)
    row = ceil(msg_len / col)
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    k_indx = 0
    msg_indx = 0
    msg_lst = list(cipher)
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError as e:
        raise TypeError("This program cannot",
                        "handle repeating words.") from e
    null_count = msg.count('_')
    if null_count > 0:
        return msg[: -null_count]
    return msg


cipher = encryptMessage(msg)
print("Encrypted Message :", cipher)
decipher = decryptMessage(cipher)
print("Decryped Message :", decipher)
