# Created by Marina Dunn on 6/19/20
# W18 Intro to Python for Data Science, UC Berkeley Summer 2020
# Homework 2

def palindrome(name):
    # makes all letters in string lowercase
    name = name.lower()
    print (name)
    first = 0
    last = len(name)-1
    # checks if first and last elements in name are equal, then continues throughout name until done with comparison
    while first < last:
        if name[first] == name[last]:
            first = first + 1
            last = last - 1
            print("Palindrome!")
            break
        else:
            print("Not a palindrome")
            break
# asks for name, then calls palindrome-checking function
name = raw_input("Enter your name: ")
palindrome(name)

# Easier way: use the reverse function to check if the string is equal to the reversed string