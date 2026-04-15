# Find sum of first N natural numbers

def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n-1)
n = int(input('Enter a number :'))
print('Sum :',sum_natural(n))