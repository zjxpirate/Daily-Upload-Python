
my_list = ['apple', 'banana', 'grapes', 'pear']

#ordinary enumeration
for counter, value in enumerate(my_list):
    print(counter, value)


print("\n")


#enumeration start from 1
for c, value in enumerate(my_list, 1):
    print(c, value)


print("\n")


#enumerate tuple
counter_list = list(enumerate(my_list, 1))
print(counter_list)

