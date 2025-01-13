# Write a Python program to remove the characters which have odd index values of a given string.

def remove_odd_value(string):
    string = string[::2]
    return string

sentence = input("Enter the input :- ")
result = remove_odd_value(sentence)

print(f"Give String:- {sentence}\nFinal String:- {result}")