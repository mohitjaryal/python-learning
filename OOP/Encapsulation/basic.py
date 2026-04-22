# ATM Machine Program

class Atm:

    # Constructor
    def __init__(self):
        self.pin = ''
        self.__balance = 0   # private attribute
        self.menu()

    # getter
    def get_balance(self):
        return self.__balance
    
    # setter
    def set_balance(self,new_value):
        if type(new_value) ==int:
            self.__balance = new_value
        else:
            print('Mat kr lala mt kr')
    

    # Menu function
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

    # Create PIN
    def create_pin(self):
        self.pin = input('Enter your PIN: ')
        self.__balance = int(input('Enter your balance: '))
        print('PIN created successfully')

    # Change PIN
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

    # Check balance
    def check_balance(self):
        if self.pin == '':
            print("Please create a PIN first")
            return

        user_pin = input('Enter your PIN: ')

        if user_pin == self.pin:
            print('Your balance is:', self.__balance)
        else:
            print('Incorrect PIN')

    # Withdraw money
    def withdraw(self):
        if self.pin == '':
            print("Please create a PIN first")
            return

        user_pin = input('Enter your PIN: ')

        if user_pin == self.pin:
            amount = int(input('Enter the amount to withdraw: '))

            if amount <= self.__balance:
                self.__balance -= amount
                print('Withdrawal successful')
                print('Remaining balance:', self.__balance)
            else:
                print('Insufficient balance')
        else:
            print('Incorrect PIN')

    # Getter method for balance (safe access)
    def get_balance(self):
        return self.__balance


# Create object
obj = Atm()

print(obj.get_balance())