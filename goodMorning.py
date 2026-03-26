# WAP to greet the user according to time

import time

# taking user's name
name = input('Enter your name :')

# hours
hour = int(time.strftime('%H'))
print('Current time :',hour)

if 5<= hour < 12:
    print('Good morning Mr ',name)
elif 12<= hour < 17:
    print('Good Afternoon Mr ',name)
elif 17 <= hour < 21:
    print('Good Evening Mr ',name)
else:
    print('Good Night Mr ',name)