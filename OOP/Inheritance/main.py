# Class Relationship
# Two types of relationships -> 1. Aggregation and 2. Inheritance

# Aggregation -> Means Has a relationship (One class own's the other class)

# class
class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.address = address
        self.gender = gender

    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)
    
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state)

# address class
class Address:
    def __init__(self,city,pin,state):
        self.__city = city
        self.pin = pin
        self.state = state
    
    # getter
    def get_city(self):
        return self.__city

    # edit address method
    def edit_address(self,new_city,new_pin,new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state

# address class object
add1 = Address('Chandigarh',189020,'Chandigarh')

# customer class's object -> passing object (add1) to Customer class
cust = Customer('Mohit','male',add1)

cust.print_address()

cust.edit_profile('mohit','mumbai',111111,'maharastra')
cust.print_address()