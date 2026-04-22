# Instance variable is -> object's variable
# Static variable is -> Class's variable

# Class definition
class Atm:

# static variable
    __counter = 1

    # Constructor: automatically runs when object is created
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        self.cid = Atm.__counter
        Atm.__counter +=1

    # getter -> this is a method of a class
    # this is a static method
    # we can access static mehtod by using class name
    # utility functions
    @staticmethod
    def get_counter():
        return Atm.__counter

    # Menu function (runs continuously using loop)
    def menu(self):
        while True:
            user_input = input("""
Hi, how can I help you?
1. Press 1 to create PIN
2. Press 2 to change PIN
3. Press 3 to check balance
4. Press 4 to withdraw
5. Press 5 to exit
""")

            # Conditions based on user input
            if user_input == '1':
                self.create_pin()

            elif user_input == '2':
                self.change_pin()

            elif user_input == '3':
                self.check_balance()

            elif user_input == '4':
                self.withdraw()

            elif user_input == '5':
                print("Thank you for using the ATM")
                break

            else:
                print("Invalid option, please try again")

    # Function to create PIN
    def create_pin(self):
        self.pin = input('Enter your PIN: ')
        self.balance = int(input('Enter your balance: '))
        print('PIN created successfully')

    # Function to change PIN
    def change_pin(self):
        if self.pin == '':
            print("Please create a PIN first")
            return

        old_pin = input('Enter old PIN: ')

        if old_pin == self.pin:
            self.pin = input('Enter new PIN: ')
            print('PIN changed successfully')
        else:
            print("Incorrect PIN, try again")

    # Function to check balance
    def check_balance(self):
        if self.pin == '':
            print("Please create a PIN first")
            return

        user_pin = input('Enter your PIN: ')

        if user_pin == self.pin:
            print('Your balance is:', self.balance)
        else:
            print('Incorrect PIN')

    # Function to withdraw money
    def withdraw(self):
        if self.pin == '':
            print("Please create a PIN first")
            return

        user_pin = input('Enter your PIN: ')

        if user_pin == self.pin:
            amount = int(input('Enter the amount to withdraw: '))

            if amount <= self.balance:
                self.balance -= amount
                print('Withdrawal successful')
                print('Remaining balance:', self.balance)
            else:
                print('Insufficient balance')
        else:
            print('Incorrect PIN')


# Create object of class
c1 = Atm()
c2 = Atm()
c3 = Atm()

print('c1',c1.cid)
print('c2',c2.cid)
print('c3',c3.cid)