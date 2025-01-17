# 7. Wite a python program to enter multiple values into a two lists and merge them but remove duplication of value only appear one time.
#     a. Do this with multiple ways/logics as many as you can.

lst1 = []
lst2 = []

while True:
    u_input = input("Enter the input for lst1:- ")
    if not u_input:
        break
    lst1.append(u_input)

while True:
    u_input = input("Enter the input for lst2:- ")
    if not u_input:
        break
    lst2.append(u_input)

print(lst1,lst2)
merge_list = list(set(lst1 + lst2))
print("The merge list using set is:- {}".format(merge_list))
merge_dict = list(dict.fromkeys(lst1+lst2))
print("The merge list using dictionary is:- {}".format(merge_dict))