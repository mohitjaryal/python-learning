# Abstraction means hiding implementation details and showing only the essential features of an object.
# Imp -> we can't make the object of the abstract class

from abc import ABC,abstractclassmethod

class BankApp(ABC):

    def database(self):
        print('Connected to data base')

# abstract method
# abstract method is a method that is declared but contains no implementation
        @abstractclassmethod
        def security(self):
            pass


class MobileApp(BankApp):

    def mobileLogin(self):
        print('Login sucessfull')
    
    def security(self):
        print('Secure login')
    
mob = MobileApp()
mob.database()