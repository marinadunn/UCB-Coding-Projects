# Created by Marina Dunn on 6/20/20
# W18 Intro to Python for Data Science, UC Berkeley Summer 2020
# Homework 2

# I'm importing the __future__ module, which I learned about through work, to have a more 
#updated version of the print() fxn so I can specify an end & separator

from __future__ import print_function

list = []
def pascal(n):
    if n > 0:
        for line in range(n):
            list.append([])
            # first element will always be 1
            list[line].append(1)
            
            for i in range(1, line):
                list[line].append(list[line-1][i-1] + list[line-1][i])
            if n != 0:
                list[line].append(1)
                
            # formats output to be an actual triangle   
            print("   " * (n - line), end = " ", sep = " ")

            for i in range(0, line+1):
                # formats output to be an actual triangle
                print('{0:6}'.format(list[line][i]), end = " ", sep = " ")
            print()
            
    # need positive number of rows
    else:
        print("invalid, try again")

# takes in user-defined number of rows then calls function to create pascal's triangle for that many rows
n = int(input("Enter number of rows: "))
pascal(n)