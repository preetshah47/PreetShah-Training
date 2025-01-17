# 4. Write a python program to add integer values into a list.
#     Add value at the beginning of the list if the value is odd.
#     Add value at the end of the list if the value is even.

lst = input("Enter the elements for list:- ").split()
lst = [int(x) for x in lst] 
print(lst)
x = int(input("Enter the value to add to the list:- "))
if x % 2 == 0 :
    lst.append(x)
else:
    lst.insert(0,x) 
print(f"The number entered is {x} & the resultant list is :- {lst}")