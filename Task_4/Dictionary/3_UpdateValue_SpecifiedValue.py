# Write a python program to update a value in a dictionary with a specified Value.

dct = {}
n = int(input("Enter the number of key value pairs:- "))

for i in range(n):
    key = input("Enter the Key:- ")
    Value = input("Enter the Value:- ")
    dct[key] = Value

print("Original Dictionary:- ", dct)


Value_input = input("Enter the Value input you want to update the value:- ")
Update_Value = input("Enter the value you want to update:- ")

for key,value in dct.items():
    if value == Value_input:
        dct[key] = Update_Value

print("Updated Dictionary:- ", dct)
