# Multilevel inheritance

class Product:
    def review(self):
        print('Customer review')


class Phone(Product):
    def __init__(self,price,brand,customer):
        print("Inside Phone's constructor")
        self.__price = price
        self.brand = brand
        self.customer = customer

    def buy(self):
        print('Buying a phone')


class SmartPhone(Phone):
    pass


# oject of SmartPhone class
s = SmartPhone(30000,'Apple',108)
s.buy()
s.review()