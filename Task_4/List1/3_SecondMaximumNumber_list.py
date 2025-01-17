# Write a python program to find the second maximum number from a list of numbers.

lst = input("Enter the elements for list:- ").split()
lst = [int(x) for x in lst] 
print(lst)
lst.sort()
print(lst[-2])
