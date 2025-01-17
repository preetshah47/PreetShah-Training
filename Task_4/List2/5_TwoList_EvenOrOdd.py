# 5. Manage two lists to store an integer values.
#     a. Enter value from user
#     b. If the value is odd number then store that number into first list
#     c. If the value is even number then store that number into second list
#     d. At the end print both list
#     e. Also print one maximum number out of two lists

lst1 = []
lst2 = []
while True:
    u_input = int(input("Enter the number:- "))
    if not u_input:
        break
    if u_input % 2 == 0:
        lst2.append(int(u_input))
    else:
        lst1.append(int(u_input))

print(f"Odd number containing list : {lst1}\nEven number containing list : {lst2}")
lst1.sort()
lst2.sort()
print(f"Maximum number for the followin list :- \nOdd List :- {lst1[-1]} \nEven List :- {lst2[-1]}")