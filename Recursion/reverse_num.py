# Print numbers from N to 1 using recursion

def display(n):
    if n == 0:
        return
    print(n)
    display(n-1)

# taking user input
n = int(input("Enter a number: "))
display(n)