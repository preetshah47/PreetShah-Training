# 3. Enter only integer values into a list from user. Keep adding the value until user enters nothing, 
#     a. If user’s entered value is not integer then give a warning message to user that the entered value is not integer and then ask for new value.
#     b. At the end print the list with all its integer value(Type of those values must be integer)

lst = []
while True:
    u_input = input("Enter the input:- ")
    if not u_input:
        break
    if u_input.isdigit():
        lst.append(int(u_input))
    else:
        print("Warning : The Entered Value is not integer. Enter New Value:- \n")

print(f"Entered list is :- {lst}")

for i in lst:
    print(f"Entered Value of list :- {i} & type:- {type(i)}")
    