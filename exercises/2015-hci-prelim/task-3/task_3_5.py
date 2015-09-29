def Encrypt(message, cipher):
    plain_to_cipher = dict()
    ordinal = 97
    for c in cipher:
        plain_to_cipher[chr(ordinal)] = c
        ordinal += 1

    enc_message = ""
    for c in message:
        if c in plain_to_cipher:
            enc_message += plain_to_cipher[c]
        else:
            enc_message += c

    return enc_message
