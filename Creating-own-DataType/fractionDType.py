# Creating our own fraction data type

# creating class
class Fraction:

    # parameterized constructor
    def __init__(self,x,y):
        self.num = x
        self.den = y

    # magic method
    def __str__(self):
        return '{} / {}'.format(self.num,self.den)
    
    # magic method
    def __add__(self, other):
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den
        return Fraction(new_num,new_den)  
    
    # magic method
    def __sub__(self, other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den
        return Fraction(new_num,new_den)
    
    # magic method
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den*other.den
        return Fraction(new_num,new_den)
    
    # magic method
    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den*other.num
        return Fraction(new_num,new_den)

# creating object
f1 = Fraction(3,4)
f2 = Fraction(1,2)

print(f1 + f2) 
print(f1 - f2) 
print(f1 * f2) 
print(f1 / f2) 