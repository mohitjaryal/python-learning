# Parent class
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside parent's constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a phone')

# Child class
class SmartPhone(Phone):
    # constructor of child class
    def __init__(self, price, brand, camera,os,ram):
        print("Inside child's constructor")
        super().__init__(price, brand, camera) # we can only access methods using super() not attributes
        self.os = os
        self.ram = ram
        print("Inside child's constructor")

s = SmartPhone(20000,'Samsung',108,'Android',16)
print(s.os)
print(s.ram)