# Store dictionary in file with using open function and write and read the file.

dct = {}

print("Enter the details to be written in file:- ")
while True:
    n = int(input("Enter the number of key-value pairs:- "))
    for i in range(n):
        key = input("Enter the key:- ")
        value = input(f"Enter the value for {key}:- ")
        dct[key] = value
    print("Dictionary:- {}".format(dct))
    break

text_file = ""

for key,value in dct.items():
    text_file += f"{key} : {value}\n"

text_file = text_file.rstrip(",")

with open('Python/Task_5_Open/text_file.txt','a') as file:
    file.write(text_file)

f = open('Python/Task_5_Open/text_file.txt','r') 
print(f.read())
    