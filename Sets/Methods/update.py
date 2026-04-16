# update method in set

s1 = {1,2,3}
s2 = {4,5,6}

# storing the value of s2 in s1 (values that are not present in s1)
result = s1.update(s2) # all the values of s2 that are not present in s1 will be added to s1

# printing the result
print('Result :',result)

print('s1:',s1)
print('s2:',s2)