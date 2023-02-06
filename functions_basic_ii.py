# Countdown
def countdown(num):
    new_list = []
    for i in range(num,0,-1):
        new_list.append(i)
    print(new_list)
countdown(10)

#Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
print_and_return([5,10])

#First Plus Length
def first_and_list(list):
    return list[0] + len(list)
print(first_and_list([7,3,2,1,10]))

# Values Greater than Second
def greater_than_second(list):
    new_list = []
    for i in range(len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    return new_list
print(greater_than_second([6,2,1,1,4,7]))

# This Length, That Value
def length_and_value(size,value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list
print(length_and_value(3,5))   