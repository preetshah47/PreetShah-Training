# Write a Python program to remove unwanted characters from a given string.

def remove_character(string,character):
    for i in character:
        string = string.replace(i, '')
    return string

sentence = input("Enter the Sentence:- ")
character = input("Enter the character:- ")

result = remove_character(sentence,character)

print(f"Given String:- {sentence}\nRemoved_string:- {result}")