# wap to find the average of number using function
def average(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total / len(numbers)


# Taking multiple inputs from user
nums = list(map(int, input("Enter numbers separated by space: ").split()))

print('Average is :',average(*nums))