# Write a python program to manage multiple values for the same key in dictionary.
# Enter key and value into dictionary.
# If the entered key already exist then do not overwrite the existing value of that key instead add both value into a list and place that list as a value of the entered key.

dct = {}

while True:
    n = int(input("\nEnter the Number of key-value pairs:- "))
    if n == 0:
        break
    for i in range(n):
        key = input("Enter the key:- ")
        value = input(f"Enter the value for {key}:- ")

        if key in dct:
            if isinstance(dct[key],list):
                dct[key].append(value)
            else:
                dct[key] = [dct[key],value]
        else:
            dct[key] = value

print("Final Dictionary:- ", dct)
    