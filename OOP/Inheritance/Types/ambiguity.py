# Ambiguity means confusion when it’s not clear which method or property should be used.

# parent class 1
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print('Buy a phone')

class Product:
    def buy(self):
        print('Product by method')
    

# pehly jiska name hoga uski first priority hogi
# this is known as method resolution order
class SmartPhone(Phone,Product):
    pass

# object
s = SmartPhone(20000,'Apple',108)
s.buy()