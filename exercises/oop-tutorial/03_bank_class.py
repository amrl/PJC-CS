class BankTransaction():

    '''
    Class representing tha main bank account for a user, which itself can
    contain multiple sub-accounts
    '''

    def __init__(self):
        '''Parameters: None'''

        self.account = []
        self.count = 0

    def openAcc(self):
        '''
        Opens an account for the object
        Parameters: None
        '''

        self.account.append(0)
        self.count += 1

        print("Account #{0} created.".format(self.count))

    def closeAcc(self, acc_no):
        '''
        Closes an account for the object. Replaces element in list with
        "CLOSED".
        Parameter: 1.Account number to close (digit)
        '''

        if str(acc_no).isdigit() == False or acc_no > len(self.account):
            print("Error: Invalid account #{0}.".format(acc_no))
            return

        self.account[acc_no - 1] = "CLOSED"
        print("Account #{0} closed.".format(acc_no))

    def addFunds(self, acc_no, amount):
        '''
        Adds an amount to an account.
        Parameters: 1.Account number (digit), 2.Amount (numeric)
        '''

        if (str(acc_no).isdigit() == False or acc_no > len(self.account) or
                self.account[acc_no - 1] == "CLOSED"):
            print("Error: Invalid account #{0}.".format(acc_no))
            return

        if str(amount).isnumeric() == False:
            print("Error: Invalid amount.")
            return

        self.account[acc_no - 1] += amount
        print("${0} added to Account #{1}.".format(amount, acc_no))

    def removeFunds(self, acc_no, amount):
        '''
        Removes an amount from an account. Error if funds not sufficient.
        Parameters: 1.Account number (digit), 2.Amount (numeric)
        '''

        if (str(acc_no).isdigit() == False or acc_no > len(self.account) or
                self.account[acc_no - 1] == "CLOSED"):
            print("Error: Invalid account #{0}.".format(acc_no))
            return

        if str(amount).isnumeric() == False:
            print("Error: Invalid amount.")
            return

        if amount > self.account[acc_no - 1]:
            print("Error: Insufficient funds to remove.")
            return

        self.account[acc_no - 1] -= amount
        print("${0} removed from Account #{1}.".format(amount, acc_no))

    def transferFunds(self, acc_no, to, amount):
        '''
        Transfers an amount from one account to another.
        Parameters: 1.Account number to transfer from (digit), 2.Account
        number to transfer to (digit), 3.Amount (numeric)
        '''

        if (str(acc_no).isdigit() == False or acc_no > len(self.account) or
                self.account[acc_no - 1] == "CLOSED"):
            print("Error: Invalid account #{0}.".format(acc_no))
            return

        if (str(to).isdigit() == False or acc_no > len(self.account) or
                self.account[to - 1] == "CLOSED"):
            print("Error: Invalid account #{0}.".format(to))
            return

        if str(amount).isnumeric() == False:
            print("Error: Invalid amount.")
            return

        self.account[to - 1] += amount
        self.account[acc_no - 1] -= amount
        print("${0} transfered from Account #{1} to Account #{2}."
              .format(amount, acc_no, to))

    def report(self, *args):
        '''
        Gives a status report of Accounts specified.
        Parameter(s): 1.Account number(s) (digit)
        '''

        for acc_no in args:
            # from account
            if str(acc_no).isdigit() == False or acc_no > len(self.account):
                print("Error: Invalid account #{0} as input.".format(acc_no))
                return

        for acc_no in args:
            if str(self.account[acc_no - 1]).isnumeric()() == True:
                print("Account #{0}: ${1}"
                      .format(acc_no, self.account[acc_no - 1]))
            else:
                print("Account #{0}: {1}"
                      .format(acc_no, self.account[acc_no - 1]))
