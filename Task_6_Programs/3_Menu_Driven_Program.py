# Create a menu driven program for managing operations that are given below.

# Menuitem:
# Display My Number
# Add into My Number
# Subtract from My Number
# Multiply with My Number
# Divide My Number
# 	Note : 
# ‘My Number’ will be default number which will be initially zero(0) when the program will start its execution.
# After performing the operation the result must be displayed and stored in ‘My Number’ variable(or object) so it can be displayed at any time from the menu.

My_Number = 0
def menu():
    print("\n1. Display My Number \n2.Add into My Number \n3.Subtract into My Number \n4.Multiplay with My Number \n5.Divide My Number \n6. Exit")

def display():
    print("Displayed Number is :- ",My_Number)

def add():
    global My_Number
    x = int(input("Enter the number to perform addition:-  "))
    My_Number += x
    print("My number after addition is :- ", My_Number)
    
def sub():
    global My_Number
    x = int(input("Enter the number to perform subtraction:-  "))
    My_Number -= x
    print("My number after subtraction is :- ", My_Number)
    
def multiply():
    global My_Number
    x = int(input("Enter the number to perform Multiplication:-  "))
    My_Number *= x
    print("My number after Multiplication is :- ", My_Number)
    
def division():
    global My_Number
    x = int(input("Enter the number to perform division:-  "))
    if x == 0:
        print(f"Dividing {My_Number} with 0 is invalid")
    else:
        My_Number /= x
        print("My number after division is :- ", int(My_Number))




while True:

    menu()    

    choice = int(input("Enter your choice:- "))

    if choice == 1:
        display()

    elif choice == 2:
        add()
        
    elif choice == 3:
        sub()

    elif choice == 4:
        multiply()

    elif choice == 5:
        division()

    elif choice == 6:
        print("Program Ended")
        break


