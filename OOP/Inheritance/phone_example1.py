# Inheritance example

# Parent class 
class Phone:
    def __init__(self,price, brand, camera):
        print('Inside Parent constructor')
        self.price = price
        self.brand = brand
        self.camera = camera
    
    # Buy method
    def Buy(self):
        print('Buying a phone')

# If child class dosen't have any constructor then automatically Parent's class constructor is called 

# Child class
class SmartPhone(Phone):
    pass

# object
s = SmartPhone(20000,'Apple',13)
