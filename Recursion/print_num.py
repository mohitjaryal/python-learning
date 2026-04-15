# Print numbers from 1 to N using recursion

def display(n):
    if n == 0:
        return
    display(n-1)
    print(n)

# taking user input
n = int(input("Enter a number: "))
display(n)