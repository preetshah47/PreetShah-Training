# # 5. Write a python program to find and count how many times value is repeated in the list.
#     - lst = [1,2,3,4,5,4,3,5,3,1,3,5,7,6,3,2,1,5,7,6,6]
#     Result :
#     - result = [(1,3),(2,2),(3,5),(4,2),(5,4),(7,2),(6,3)]

lst = input("Enter the elements for list:- ").split()
lst = [int(x) for x in lst] 
print(f"Entered list is : {lst}")

count_dict = {}

for i in lst:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

result = list(count_dict.items())
print("Result: {}".format(result))



