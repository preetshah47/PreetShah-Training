# Write a Python program to remove extra spaces from a given string(remove beginning and end spaces but keep one space in between words).

def spaceremover(string):
    return " ".join(string.split())
    # return string

string = "Okay Dokey    Okay    Dokey"
result = spaceremover(string)

print("This is the final string:-  ", result)