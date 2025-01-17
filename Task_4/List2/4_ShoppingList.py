# 4. Manage a shopping list with python list,
#     a. Enter shopping item from user into a list,
#     b. Keep asking for item names until user enters nothing.
#     c. At the end print the list.

shopping_list = []
while True:
    s_list = input("Enter the item name:- ")
    if not s_list:
        break
    shopping_list.append(s_list)
print("The Entered Shopping list is :- {}".format(shopping_list))