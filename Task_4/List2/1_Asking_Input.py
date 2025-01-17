# 1. Simple way to keep asking user for input it stops until user enters nothing.

while True:
    x = input("Enter any input:- ")
    if not x:
        break
    print("Your Entered value is : {}".format(x))