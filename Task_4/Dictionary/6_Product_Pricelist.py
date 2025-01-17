# Write a python program to manage product’s pricelist.
# Keep asking for key until the user enters nothing.
# Enter product(key) and its price(value)
# Entering key that is already added it should update the value with available key value pair.
# Print the dictionary in tabular format

dct = {}
n = int(input("Enter the number of key-value pairs:- "))
for i in range(n):
    key = input("Enter the product:- ")
    value = input(f"Enter the price for {key}:- ")
    dct[key] = value
print(f"{'Product':<20} {'value':<10}")
for key,value in dct.items():
    print(f"{key:<20}{value:<10}")
