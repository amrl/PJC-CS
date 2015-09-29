from task_3_1 import CreateCipher
from task_3_3 import Decrypt


infile = open("CIPHER.txt", "r")
phrase = infile.readline()[:-1]
enc_message = infile.readline()[:-1]
infile.close()

dec_message = Decrypt(enc_message, CreateCipher(phrase))
print("Phrase: {0}".format(phrase))
print("Encrypted message: {0}".format(enc_message))
print("Decrypted message: {0}".format(dec_message))
