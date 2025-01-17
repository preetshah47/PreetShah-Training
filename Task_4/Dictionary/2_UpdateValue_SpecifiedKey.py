# Write a python program to update a value in a dictionary with a specified key.

dct = {}
n = int(input("Enter the number of key value pairs:- "))

for i in range(n):
    key = input("Enter the Key:- ")
    Value = input("Enter the Value:- ")
    dct[key] = Value

print("Original Dictionary:- ", dct)


key_input = input("Enter the key input you want to update the value:- ")
Update_Value = input("Enter the value you want to update:- ")

for i in dct.keys():
    if i == key_input:
        dct[i] = Update_Value

print("Updated Dictionary:- ", dct)
