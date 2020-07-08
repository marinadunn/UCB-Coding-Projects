# Created by Marina Dunn on 6/19/20
# W18 Intro to Python for Data Science, UC Berkeley Summer 2020
# Homework 2

def tax(income):
    # if user falls under first cut-off
    if 0 <= income and income <= 1000:
        tax = income * .05
    # if user falls under second cut-off
    elif 1000 < income < 2000:
        tax = (income - (1000*.05)) * .10
    # if user has income higher than cut-offs
    elif income >= 2000:
        tax = income * .15
    else:
        pass
    print (tax)

# asks user for income then calls tax calculator function
income = int(input("Please enter your income:"))
tax(income)