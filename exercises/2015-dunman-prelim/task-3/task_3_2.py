from task_3_1 import ISBN_Check_Digit


def Valid_ISBN(isbn):
    check_digit = isbn[-1]
    isbn_no_check_digit = isbn[:-1]

    if check_digit == ISBN_Check_Digit(isbn_no_check_digit):
        return True
    else:
        return False


# Tests
# print(Valid_ISBN("0-07-063546-3"))      # valid
# print(Valid_ISBN("978-0-07-063546-3"))  # valid
# print(Valid_ISBN("0-07-063546-9"))      # invalid
# print(Valid_ISBN("978-0-07-063546-9"))  # invalid
