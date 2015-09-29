def CreateCipher(phrase):
    key = ""
    for c in phrase:
        if c.upper() not in key:
            key += c.upper()

    cipher_text_alphabet = key
    ordinal = 65
    while ordinal <= 90:
        if chr(ordinal) not in cipher_text_alphabet:
            cipher_text_alphabet += chr(ordinal)
        ordinal += 1

    return cipher_text_alphabet


# print(CreateCipher("apple"))
