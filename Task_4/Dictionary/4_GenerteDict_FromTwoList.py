# Write a python program to generate a dictionary from two lists
# customer = [‘Bhaskar’, ’Vishal’, ‘Dhara’]
# items = [[‘apple’,’orange’], [‘banana’,’weat floor’], [‘butter milk’,’apple juice’]]
# Receive this two lists from user
# And create one dictionary like below.
# {Bhaskar’: [‘apple’,’orange’], ‘Vishal’: [‘banana’,’weat floor’], ‘Dhara’: [‘butter milk’,’apple juice’]}

customer = []
items = []
dct = {}

while True:
    u_input = input("Enter the input for customer:- ")
    if not u_input:
        break
    customer.append(u_input)

    item = []
    while True:
        u_input = input("Enter the input for items:- ")
        if not u_input:
            break
        item.append(u_input)
    items.append(item)

for i in range(len(customer)):
    dct[customer[i]] = items[i]

print("Shopping list in the form of dictionary :- ", dct)



