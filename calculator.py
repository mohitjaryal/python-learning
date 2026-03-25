# basic calcuator using python

num1 = int(input('Enter number 1:'))
num2 = int(input('Enter number 2:'))

# which operation user wants to perform
operation = int(input('Enter which operation you want to perform \n1. + \n2. - \n3. * \n4. / \n :'))

# main logic
if operation == 1:
    print('Sum :', num1 + num2)
elif operation == 2:
    print('Subtraction :', num1-num2)
elif operation == 3:
    print('Multiplication :', num1 * num2)
elif operation == 4:
    print('Division :', num1 / num2)
else:
    print('Error occured ! \n Please try again')