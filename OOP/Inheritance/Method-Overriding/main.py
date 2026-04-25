""" Method overriding 
if there is inheritance and we have mehthods with same names in both child and parent class then the method of 
child class will execute
"""

# Parent class
class Phone:
    def __init__(self,price,brand,camera):
        print('Inside the constructor')
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print('Buying a phone')

# Child class
class SmartPhone(Phone):
    def buy(self):
        print('Buying a smartphone')


s = SmartPhone(20000,'Apple',108)
s.buy()