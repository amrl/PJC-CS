# get data from file
infile = open("cipher.txt", 'r')
key_phrase = infile.readline()[:-1].upper()
message = infile.readline()[:-1]
infile.close()

# get key from key phrase by removing all repeated letters
key = ""
for c in key_phrase:
    if c not in key:
        key += c

d = {}  # {cipher_alphabet : plain_alphabet, ...}
# populate conversion dictionary...

# ...for ciphertext alphabets in key
plain_ord = 97  # start from 'a'
for cipher_alphabet in key:
    d[cipher_alphabet] = chr(plain_ord)
    plain_ord += 1

# ...for remaining ciphertext alphabets
cipher_ord = 65  # start from 'A'
while plain_ord <= 122:  # last plaintext alphabet is 'z'
    cipher_alphabet = chr(cipher_ord)
    if cipher_alphabet not in key:
        d[cipher_alphabet] = chr(plain_ord)
        plain_ord += 1

    cipher_ord += 1

# use dict d to decrypt message
decrypted = ""
for c in message:
    if c in d:
        decrypted += d[c]
    else:
        decrypted += c  # non-alphabets (no decryption)

# display results
print('***')
print(key)
print(decrypted)
print('***')
