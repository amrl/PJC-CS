from task_3_1 import CreateCipher


def CreateCipherTest():
    infile = open("PHRASES.txt", "r")
    for line in infile:
        phrase = line[:-1]
        cipher_text = CreateCipher(phrase)
        print("Phrase: {0}".format(phrase))
        print("Cipher text: {0}".format(cipher_text))
    infile.close()


# CreateCipherTest()
