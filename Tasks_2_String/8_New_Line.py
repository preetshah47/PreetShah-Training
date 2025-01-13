# Write a Python program to receive a string from the user and ask the user to add after which characters he/she wants to add a new line character.

def New_Line(string,word):
    for i in word:
        string = string.replace(i, i + "\n")
    return string   
    
sentence = input("Enter the sentence:- ")
word = []

while True:
    insert = input("Enter the word:- ")
    if not insert:
        break
    word.append(insert)

result = New_Line(sentence,word)

print(f"Given String:- {sentence}\nFinal String:- \n{result}")