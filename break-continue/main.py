# program to demonstrate break and continue statement

# user input
num = int(input('Enter a number :'))
skip1 = int(input('Enter a number that you want to skip :'))
end = int(input('Enter a number at which you want to end the loop :'))

# loop
for i in range(num):
    if i == skip1:
        continue
    if i == end:
        break
    print(i)