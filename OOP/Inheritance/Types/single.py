# Single level inheritance
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside parent's constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a phone')

class SmartPhone(Phone):
    pass

s = SmartPhone(20000,'Apple',108)
s.buy()
