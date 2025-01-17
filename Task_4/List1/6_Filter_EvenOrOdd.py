# 6. Write a python program to filter out the list of numbers that are odd and even
#     - lst = [1,2,3,4,5,6,7,8,9]
#     Result :
#     - odd_numbers = [1,3,5,7,9]
#     - even_numbers = [2,4,6,8]

lst = input("Enter the elements for list:- ").split()
lst = [int(x) for x in lst] 
print(lst)
odd_numbers = []
even_numbers = []
for i in lst:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(f"Result: - \neven_numbers = {even_numbers}\nodd_numbers = {odd_numbers}")

