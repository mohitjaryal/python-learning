# hierarchical inheritance

class Phone:
    def __init__(self,price,brand,customer):
        print("Inside phone's constructor")
        self.__price = price
        self.brand = brand
        self.customer = customer

    def buy(self):
        print('Buying a phone')

class SmartPhone(Phone):
    pass

class Feature(SmartPhone):
    pass

# SmartPhone class's object
s = SmartPhone(20000,'Apple',108)
s.buy()

# Feature class's object
f = Feature(10000,'Samsung',200)

f.buy()