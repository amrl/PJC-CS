from task_3_1 import ISBN_Check_Digit


def ISBN10_To_ISBN13(isbn):
    isbn = "978-" + isbn
    check_digit = ISBN_Check_Digit(isbn)
    isbn13 = isbn + "-" + check_digit

    return isbn13


# print(ISBN10_To_ISBN13("0-07-063546"))
