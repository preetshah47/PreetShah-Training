
# Create a python program to manage shopping list.
# Take input from user
# This process must not stop unless user enters nothing
# Use functions/methods to manage each operation
# Manage validations such as if the item not found
# On 8th option display list in tabular format
# 	Inputs :
# 		1 Add an item
# 		2 Add multiple items
# 		3 Add an item at index
# 		4 Remove last added item
# 		5 Remove an item with name
# 		6 Remove all items/ Empty list
# 		7 Replace an item with new item
# 		8 Display list

from tabulate import tabulate

shopping_list = []

def menu():
    print("\n1. Add an item \n2.Add Multiple items \n3.Add an item at index \n4.Remove last added item \n5.Remove an item with name \n6. Remove all items/ Empty list \n7. Replace an item with new item \n8.Display List \n9.Exit")

def display_list():
    if shopping_list:
        table = [[index + 1, item] for index, item in enumerate(shopping_list)]
        print(tabulate(table, headers=["S.No", "Item Name"], tablefmt="grid"))
    else:
        print("Shopping list is empty, please add items to the list!")

def add_one_item():
    item = input("Enter one item to add to the shopping list:- ")
    shopping_list.append(item)
    if item:
        print(f"{item} item is added to the shopping list")
    else:
        print("No item is added")

def add_multiple_item():
    items = input("Enter multiple items to the shopping list:- ").split(",")
    shopping_list.extend(item.strip() for item in items)
    print("Items are added to the list.")

def Insert_Item_SpecificPosition():
    item = input("Enter one item to insert to the shopping list:- ")
    if item:
        position = int(input("Enter the position you want to insert the item in the shopping list:- "))
        shopping_list.insert(position - 1,item)
    else:
        print("No item is inserted.")

def Remove_last_item():
    if shopping_list:
        r_item = shopping_list.pop()
        print(f"{r_item} is removed from the shopping list.")
    else:
        print("The shopping list is already empty.")

def Remove_item_name():
    item = input("Enter the item to be removed from the shopping list:- ")
    if item in shopping_list:
        shopping_list.remove(item)
        print("{} is removed from the list".format(item))
    else:
        print("Entered item is not present in the list.")

def Empty_List():
    shopping_list.clear()
    print("The shopping list is now empty.")

def Replace_item_with_new_item():
    r_item = input("Enter the item you want to replace:- ")
    if r_item in shopping_list:
        item = input(f"Enter the item you want to replace {r_item} with:- ")
        index = shopping_list.index(r_item)
        shopping_list[index] = item
        print(f"{r_item} is replaced with {item}")
    else:
        print(f"{r_item} is not found in shopping list")
        

while True:
    menu()
    choice = int(input("Enter your choice:- "))

    if choice == 8:
        display_list()
    elif choice == 1:
        add_one_item()
    elif choice == 2:
        add_multiple_item()
    elif choice == 3:
        Insert_Item_SpecificPosition()
    elif choice == 4:
        Remove_last_item()
    elif choice == 5:
        Remove_item_name()
    elif choice == 6:
        Empty_List()
    elif choice == 7:
        Replace_item_with_new_item()
    elif choice == 9:
        print("Program Ended")
        break
    else:
        print("Please enter valid choice!")