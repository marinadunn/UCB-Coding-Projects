# Created by Marina Dunn on 6/19/20
# W18 Intro to Python for Data Science, UC Berkeley Summer 2020
# Homework 2

def tip_calc(price):
    # has a set tip amount. if you would like to choose, see code below
    tip = price * .16
    # updated total
    total = price + tip
    print("A %16 tip would be ", tip)
    print("The total including tip would be ", total)
    # does not include tax

# takes in price and calls tip calculator function
price = float(input("Enter the price of a meal: "))
tip_calc(price)

"""
Optional if wanting to do user-desired tip:

def tip_calc(price, tip):
    new_tip = price * tip
    total = price + new_tip
    print("The tip would be ", new_tip)
    print("The total including tip would be ", total)
    
price = float(input("Enter the price of a meal: "))
tip = float(input("Enter the tip % of a meal: ")) / 100

tip_calc(price, tip)
"""