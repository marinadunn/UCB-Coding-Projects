# Created by Marina Dunn on 6/19/20
# W18 Intro to Python for Data Science, UC Berkeley Summer 2020
# Homework 2

def pig(name):
    vowels = "aeiou"
    # make all letters lowercase and split string at a space
    name = name.lower().split(' ')
    list = []
    for i in name:
        # define the first letter of the name, which decides how to apply Pig Latin rules
        first = i[0]
        # if the first letter in the name is a vowel, drop it and add ay at the end
        if len(name) > 0 and first in vowels:
            new = i[1:] + 'ay'
            # add name to list
            list.append(new)
        # if not, put the first letter at the end of the name, then add ay
        else:
            new = i[1:] + first + 'ay'
            # add name to list
            list.append(new)
    # capitalize only the first letter of each part of the name
    list = [i.capitalize() for i in list]
    # print the entire name
    print " ".join(list)
    
# takes in name of any length and calls Pig Latin function
name = raw_input("Enter your name: ")
pig(name)