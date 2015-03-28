# Same as other BankTransaction class, but now using dictionary


class BankTransaction():

    def __init__(self):
        self.accounts = {}

    def openAcc(self, name):
        if name in self.accounts:
            print("Error: Account name already in use.\n")
            return

        self.accounts[name] = 0
        print("Account", name, "opened.")

    def closeAcc(self, name):
        if name in self.accounts:
            self.accounts.pop(name)
            print("Account", name, "closed.")
        else:
            print("Error: Account name not found.")

    def addFunds(self, name, amount):
        if str(amount).isnumeric() == False:
            print("Error: Amount given must be numeric.")
            return

        if name not in self.accounts:
            print("Error: Account name not found.")
            return

        self.accounts[name] += amount
        print("${0} added to Account {1}.".format(amount, name))

    def removeFunds(self, name, amount):
        if str(amount).isnumeric() == False:
            print("Error: Amount given must be numeric.")
            return

        if amount > self.accounts[name]:
            print("Error: Amount given higher than current funds in account.")
            return

        if name not in self.accounts:
            print("Error: Account name not found.")
            return

        self.accounts[name] -= amount
        print("${0} removed from Account {1}.".format(amount, name))

    def transferFunds(self, take, give, amount):
        if str(amount).isnumeric() == False:
            print("Error: Amount given must be numeric.")
            return

        if take not in self.accounts or give not in self.accounts:
            print("Error: Account name not found.")
            return

        if amount > self.accounts[take]:
            print("Error: Amount given higher than current funds in account.")
            return

        self.accounts[take] -= amount
        self.accounts[give] += amount
        print("${0} transfered from Account {1} to Account {2}."
              .format(amount, take, give))

    def report(self):
        for key in self.accounts:
            print("Account {0}: ${1}".format(key, self.accounts[key]))
