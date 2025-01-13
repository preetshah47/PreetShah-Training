# Write a Python program to receive a string input from user and if there are any special character such as \n or \t then program should print the entered string with new line and with a tabular space


def special_characters(string):
    return string.replace("\\n","\n").replace("\\t","\t")


sentence = input("Enter the sentence:- ")
result = special_characters(sentence)

print(f"Given String:- {sentence}\nFinal String:- \n{result}")
