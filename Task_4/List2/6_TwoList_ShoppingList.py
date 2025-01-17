# 6. Manage two lists, so that you can manage customer name and customer shopping list
#     a. In one list enter customer name.
#     b. In second list enter customer shopping items
#     c. So it will look like this
#         i) Lst1 = [‘Bhaskar’, ’Vishal’, ‘Dhara’]
#        ii) Lst2 = [[‘apple’,’orange’], [‘banana’,’weat floor’], [‘butter milk’,’apple juice’]]
#     d. Print the two lists like this:
#         i) Bhaskar : [‘apple’,’orange’]
#        ii) Vishal : [‘banana’,’weat floor’]
#       iii) Dhara : [‘butter milk’,’apple juice’]
# Note : Keep asking user to enter values until user enters nothing.

customer_name_list = []
customer_shopping_list = []
while True:
    customer_name_list_input = input("Enter the Customer name:- ")
    if not customer_name_list_input:
        break
    customer_name_list.append(customer_name_list_input)

    items = []
    while True:
        item = input("Enter the shopping item :- ")
        if not item:
            break
        items.append(item)
    customer_shopping_list.append(items)

for i in range(len(customer_name_list)):
    print(f"{customer_name_list[i]} : {customer_shopping_list[i]}")