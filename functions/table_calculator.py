# wap to do basic math calculation and print table according to user


# function for performing math calculations
def calculation():
    # user input for math operation
    operation = int(input('What do you want to perform : \n1. Addition \n2.Subtraction \n3. Division \n4. Multiplication :'))
    num1 = int(input('Enter first number :'))
    num2 = int(input('Enter second number :'))

    # condition check
    if operation == 1:
        print(num1 + num2)
    elif operation == 2:
        print(num1 - num2)
    elif operation == 3:
        print(num1 / num2)
    elif operation == 4:
        print(num1 * num2)
    else:
        print('Something went wrong please try again!')



# function to perform table
def table():
    num = int(input('Enter a number :'))
    # loop
    i = 1
    while i <=10:
        print(num, 'x',i, num * i)
        i += 1


# user input
work = int(input('What do you want to do sir \n1. Calculation \n2. Print Table :'))
if work == 1:
    calculation()
else:
    table()