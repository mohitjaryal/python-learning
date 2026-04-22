# instance variable -> it is a special variable which has different values for different objects

class Name:
    def __init__(self,name,country):
        self.name = name
        self.country = country
    

# creating object
p1 = Name('mohit','india')
p2 = Name('elon','usa')    

print('P1 object :',p1.name)
print('P2 object :',p2.name)