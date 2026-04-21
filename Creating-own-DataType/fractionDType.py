# Creating our own fraction data type

# creating class
class Fraction:

    # parameterized constructor -> means this is a constructor which needs an input 
    def __init__(self,x,y):
        self.num = x
        self.den = y

    # magic mehtod
    def __str__(self):
        return '{} / {}'.format(self.num,self.den)