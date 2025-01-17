# 2. Write a python program to add multiple values from user  into a list, Find out the type of a value and store that value as its type
#     a. Input will be string all the time but we can still see if it is integer value or not by string functions, use then to determine the value type and then convert the value and then store inside a list\
#     b. Keep adding the value from the user until user enters nothing.

lst = []
while True:
    u_input = input("Enter the input:- ")
    if not u_input:
        break
    if u_input.isdigit():
        lst.append(int(u_input))
    elif u_input.replace('.',"").isdigit() and u_input.count('.') == 1:
        lst.append(float(u_input))
    else:
        lst.append(u_input)
for i in lst:
    print(f"value :- {i} & type :- {type(i)}")
