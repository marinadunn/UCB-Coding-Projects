# Created by Marina Dunn on 6/19/20
# W18 Intro to Python for Data Science, UC Berkeley Summer 2020
# Homework 2

# I'm importing the __future__ module, which I learned about through work, to have a more 
#updated version of the print() fxn so I can specify an end & separator

from __future__ import print_function

def inverse_matrix(text):
    # create a list of the values by splitting, then change all to floats
    text = text.split(" ")
    textf = [float(item) for item in text]
    
    a = float(textf[0])
    b = float(textf[1])
    c = float(textf[2])
    d = float(textf[3])
    # the constant the matrix will be multiplied by
    scalar = (a*d-b*c)**-1
    
    # create tuples for inices 0-2, and 2-4, then make a tuple of those
    for num in textf:
        tup1 = [tuple(textf[:2])]
        tup2 = [tuple(textf[2:])]
        matrix = tuple(tup1 + tup2)
    print ("matrix: ", matrix)

    for i in matrix:
        rtup1 = [tuple([d,-b])]
        rtup2 = [tuple([-c, a])]
        reversed = tuple(rtup1 + rtup2)
    #print (reversed)
    
    list = [d,-b,-c, a]
    
    new = [scalar * i for i in list]
    #print (new)
    
    new_tup1 = [tuple(new[:2])]
    new_tup2 = [tuple(new[2:])]
    inverse = tuple(new_tup1 + new_tup2)
    print ("inverse: ", inverse)


# read in 4 random values, then call inverse function
text = raw_input("Enter 4 values: ")
inverse_matrix(text)