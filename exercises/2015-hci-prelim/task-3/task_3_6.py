from task_3_1 import CreateCipher
from task_3_5 import Encrypt


message = "do not give up"
phrase = "skyhigh"
enc_message = Encrypt(message, CreateCipher(phrase))
print("Phrase: {0}".format(phrase))
print("Encrypted Message: {0}".format(enc_message))
