#  1. Write a Python program to sum all the items in a list.

lst1 = [2,3,4,5,3]
lst = input("Enter the elements for list:- ").split()
lst = [int(x) for x in lst] 
print(lst)
result = 0
for i in lst1:
    result += i
print(result)
print("The sum is : ", sum(lst))