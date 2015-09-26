from task_3_1 import ISBN_Check_Digit


def ISBN13_To_ISBN10(isbn):
    isbn = isbn[3:]
    check_digit = ISBN_Check_Digit(isbn)
    isbn10 = isbn + "-" + check_digit
    if isbn10[0] == '-':  # return isbn without leading '-'
        return isbn10[1:]
    else:
        return isbn10


print(ISBN13_To_ISBN10("978-0-07-063546"))
