# check whether a number is even or odd ( using match-case )
num = int(input('Enter a number: '))

match num % 2:
    case 0:
        print(num, 'is an even number')
    case 1:
        print(num, 'is an odd number')