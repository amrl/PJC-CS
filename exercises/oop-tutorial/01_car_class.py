class Car:

    '''Class representing a car's make, model, production year, and price'''

    def __init__(self, make=None, model=None,
                 production_year=None, price=None):
        '''Parameters: make, model, production year, price'''

        self.make = make
        self.model = model
        self.year = production_year
        self.price = price

    def getMake(self):
        '''Returns car's make'''

        return self.make

    def getModel(self):
        '''Returns car's model'''

        return self.model

    def getYear(self):
        '''Returns car's production year'''

        return self.year

    def setPrice(self, price):
        '''Sets car's price. Parameter: price (numeric)'''

        self.price = price
        print("Price set to ${0}.".format(price))

    def getPrice(self):
        '''Returns car's price'''

        return self.price

    def compareWith(self, other):
        '''
        Compares current Car object with another Car object.
        Parameter: another Car object
        '''

        string = ''

        if self.make == other.make:
            string += "Both cars are from {0}.\n".format(self.make.title())
            if self.model == other.model:
                string += "Both cars are of the same model, {0}.\n" \
                          .format(self.make.title())
            else:
                string += "Car 1 is a {0} while Car 2 is a {1}.\n" \
                          .format(self.model.title(), other.model.title())
        else:
            string += "Car 1 is from {0} while Car 2 is from {1}.\n" \
                       .format(self.make.title(), other.make.title())
            string += "Car 1 is a {0} while Car 2 is a {1}.\n" \
                      .format(self.model.title(), other.model.title())

        if self.year == other.year:
            string += "Both cars were produced at the same year, {0}.\n" \
                       .format(self.year)
        elif self.year < other.year:
            string += "Car 1 is older than Car 2 by {0} year(s).\n" \
                      .format(abs(self.year - other.year))
        else:
            string += "Car 2 is older than Car 1 by {0} year(s).\n" \
                      .format(abs(other.year - self.year))

        if self.price == other.price:
            string += "Both cars are of the same price, ${0}." \
                      .format(self.price)
        elif self.price > other.price:
            string += "Car 1 is more expensive than Car 2 by ${0}." \
                      .format(self.price - other.price)
        else:
            string += "Car 2 is more expensive than Car 1 by ${0}." \
                      .format(other.price - self.price)

        print(string)
