# Created by Marina Dunn on 6/20/20
# W18 Intro to Python for Data Science, UC Berkeley Summer 2020
# Homework 2

# will use recursion method

def fibonacci(n):
    if n == 0:
        # first fibonacci number
        return 0
    elif n == 1:
        # second fibonacci number
        return 1
    else:
        # continues until unable to do fibonacci function anymore
        return (fibonacci(n-1) + fibonacci(n-2))

# takes in user-defined number, then calls fibonacci function if positive      
n = int(input("Enter a number: "))
list = []
if n < 0:
    print("invalid, enter positive number")
else:
    for i in range(0,n):
        ans = fibonacci(i)
        # updates list with fibonacci values
        list.append(ans)
    # shows only values less than the user-defined number
    res = [list[j] for j, val in enumerate(list) if val < n] 
    print (res)