# Write a Python program to multiply all the items in a list.

lst = input("Enter the elements for list:- ").split()
lst = [int(x) for x in lst] 
print(lst)
result = 1
for i in lst:
    result = result * i
print(result)