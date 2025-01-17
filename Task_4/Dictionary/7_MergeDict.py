# Write a python program to merge two dictionaries.
# Receive key and value input from user do that for 2 dictionaries.

dct1 = {}
dct2 = {}

def input_function(dct):
    while True:
        n = int(input("Enter the number of key and value pairs:- "))
        for i in range(n):
            key = input("Enter the key:- ")
            value = input(f"Enter the value for {key}:- ")
            dct[key] = value
        print(f"{dct}")
        break

print("Enter the key and value pairs for first dictionary :- ")
input_function(dct1)
print("Enter the key and value pairs for second dictionary :- ")
input_function(dct2)

dct2.update(dct1)
print("Merged Dictionary:- ",dct2)





