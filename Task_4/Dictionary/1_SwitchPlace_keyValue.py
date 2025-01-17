# Write a python program to switch places of key value in a dictionary.

ori_dict = {}
NoOfKey = int(input("Enter the number of key value pairs:- "))

for i in range(NoOfKey):
    key = input("Enter key: - ")
    value = input("Enter Value:- ")
    ori_dict[key] = value

switch_dict = {}

for key,value in ori_dict.items():
    switch_dict[value] = key

print("Original Dictionary:- ",ori_dict)
print("Switched Dictionary:- ",switch_dict)
