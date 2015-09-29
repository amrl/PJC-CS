def Decrypt(enc_message, cipher):
    cipher_to_plain = dict()
    ordinal = 97
    for c in cipher:
        cipher_to_plain[c] = chr(ordinal)
        ordinal += 1

    dec_message = ""
    for c in enc_message:
        if c in cipher_to_plain:
            dec_message += cipher_to_plain[c]
        else:
            dec_message += c

    return dec_message
