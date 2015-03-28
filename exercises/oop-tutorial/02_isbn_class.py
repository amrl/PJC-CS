class ISBN:

    '''Class representing a book's ISBN number'''

    def __init__(self, isbn="XXXXXXXXXX"):  # 10-digit
        '''Parameter: ISBN (string, empty for default)'''

        self.isbn = isbn

    def validate(self):
        '''
        Validates check number of ISBN. Returns True if correct,
        False otherwise
        '''

        if len(self.isbn) != 10:
            return False

        check = 0
        for i in range(1, 10):
            check += i * int(self.isbn[i-1])

        # 2nd method to generate check digit
        # check = 1 * int(self.isbn[0]) + 2 * int(self.isbn[1]) +
        #         3 * int(self.isbn[2]) + 4 * int(self.isbn[3]) +
        #         5 * int(self.isbn[4]) + 6 * int(self.isbn[5]) +
        #         7 * int(self.isbn[6]) + 8 * int(self.isbn[7]) +
        #         9 * int(self.isbn[8])

        digit = check % 11

        if digit == int(self.isbn[9]):
            return True
        elif digit == 10 and int(self.isbn[9]) == "X":
            return True
        else:
            return False

    def setGroup(self, group_code):  # group code 1-digit
        '''Sets Group code of ISBN. Parameter: group code (digit, 1-digit)'''

        group_code = str(group_code)
        if len(group_code) != 1 or group_code.isdigit() == False:
            return False

        self.isbn = group_code + self.isbn[1:10]
        return True

    def getGroup(self):
        '''Returns Group code of ISBN'''

        return self.isbn[0]

    def setPubCode(self, pub_code):  # publisher code 3-digit
        '''
        Sets Publisher code of ISBN. Parameter: publisher code
        (digit, 3-digits)
        '''

        pub_code = str(pub_code)
        if len(pub_code) != 3 or pub_code.isdigit() == False:
            return False

        self.isbn = self.isbn[0] + pub_code + self.isbn[4:10]
        return True

    def getPubCode(self):
        '''Returns Publisher code of ISBN'''

        return self.isbn[1:4]

    def setUnique(self, unique_code):  # unique code 5-digit
        '''
        Sets Unique code of ISBN. Parameter: unique code
        (digit, 5-digits)
        '''

        unique_code = str(unique_code)
        if len(unique_code) != 5 or unique_code.isdigit() == False:
            return False

        self.isbn = self.isbn[0:4] + unique_code + self.isbn[9]
        return True

    def getUnique(self):
        '''Returns Unique code of ISBN'''

        return self.isbn[4:9]

    def setCheck(self, check_digit):  # check digit 1-digit
        '''Sets Check digit of ISBN. Parameter: check digit (digit, 1-digit)'''

        check_digit = str(check_digit)
        if len(check_digit) != 1 and check_digit.isdigit() == False:
            return False

        self.isbn = self.isbn[0:9] + check_digit
        return True

    def getCheck(self):
        '''Returns Check digit of ISBN'''

        return self.isbn[9]

    def setISBN(self, number):
        '''Sets whole ISBN number to object. Parameter: ISBN
        (digit, 10-digits)
        '''

        number = str(number)
        if len(number) != 10 and number.isdigit() == False:
            return False

        self.isbn = number
        return True

    def __str__(self):
        '''Returns whole ISBN in format X-XXX-XXXXX-X'''

        return "{0}-{1}-{2}-{3}".format(self.isbn[0], self.isbn[1:4],
                                        self.isbn[4:9], self.isbn[9])
