# 8. Write a python program to manage shopping list.
#     a. Use list to store item name
#     b. Keep adding the items into list until user enters nothing
#     c. Perform the below operations
#         i) Display list
#        ii) Add one item into list
#       iii) Add multiple items into list
#        iv) Insert an item on a specific place into list
#         v) Remove item from list(last item)
#        vi) Remove item from list(item name)
#       vii) Empty list


def main():
    print("Enter your choice:- \ni)   Display list\nii)  Add one item into list\niii) Add multiple items into list\niv)  Insert an item on a specific place into list\nv)   Remove item from list(last item)\nvi)  Remove item from list(item name)\nvii) Empty list\nviii)To End")

shopping_list= []

def display_list():
    if shopping_list:
        print("Displaying Shopping List:- ", shopping_list)
    else:
        print("Shopping list is empty, please add item to list!")

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

while True:
    main()
    choice = int(input("Enter your choice:- "))

    if choice == 1:
        display_list()
    elif choice == 2:
        add_one_item()
    elif choice == 3:
        add_multiple_item()
    elif choice == 4:
        Insert_Item_SpecificPosition()
    elif choice == 5:
        Remove_last_item()
    elif choice == 6:
        Remove_item_name()
    elif choice == 7:
        Empty_List()
    elif choice == 8:
        print("Program Ended")
        break
    else:
        print("Please enter valid choice!")


