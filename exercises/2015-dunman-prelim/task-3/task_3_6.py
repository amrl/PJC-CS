from task_3_1 import ISBN_Check_Digit
from task_3_5 import Hash_Key
from random import randint


def Insert_Book(isbn):
    outfile = open("LIBRARY.txt", "r+")

    address, bucket = Hash_Key(isbn)
    orig_bucket = bucket
    isbn = isbn.ljust(13, '#')  # pad isbn

    outfile.seek(address*13)
    if not outfile.read(1).isdigit():
        outfile.seek(address*13)
    else:  # collision encountered
        outfile.seek(bucket*13)
        while outfile.read(1).isdigit():
            outfile.seek(bucket*13)
            bucket += orig_bucket
        outfile.seek(bucket*13)

    outfile.write(isbn)
    outfile.close()


def generate_ISBNs_and_populate(size):
    # generate list of ISBNs
    ISBNs = list()
    while len(ISBNs) <= size:
        isbn = ""
        choice = randint(0, 1)  # randomly choose to create ISBN10 or ISBN13
        if choice == 0:  # generate ISBN10
            for _ in range(9):
                digit = randint(0, 9)
                isbn += str(digit)
        else:  # generate ISBN13
            for _ in range(12):
                digit = randint(0, 9)
                isbn += str(digit)

        # append check digit
        isbn += ISBN_Check_Digit(isbn)

        if isbn not in ISBNs:
            ISBNs.append(isbn)

    # write ISBNs to outfile
    outfile = open("LIBRARY.txt", "w")  # create file first to ensure readable
    outfile.close()
    for isbn in ISBNs:
        Insert_Book(isbn)


def Lookup_Book(isbn):
    isbn = ''.join(isbn.split('-'))  # parse ISBN into string of numbers only.
    address, bucket = Hash_Key(isbn)
    orig_bucket = bucket
    found = False

    searchfile = open("LIBRARY.txt", "r")
    searchfile.seek(address*13)

    if searchfile.read(13).startswith(isbn):
        found = True
    else:
        limit = 251
        searchfile.seek(bucket*13)
        while bucket <= limit and not searchfile.read(13).startswith(isbn):
            bucket += orig_bucket
            searchfile.seek(bucket*13)

        searchfile.seek(bucket*13)
        if searchfile.read(13).startswith(isbn):
            found = True
    searchfile.close()

    return found


# generate_ISBNs_and_populate(250)
