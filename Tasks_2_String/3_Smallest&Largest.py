# Write a Python program to find the smallest and largest word in a given string.


def smallest_word(string):
    words = string.split()
    smallest = min(words, key=len)
    return smallest


def largest_word(string):
    words = string.split()
    Largest = max(words, key=len)
    return Largest

sentence = input("Enter the sentence :- ")
smallest = smallest_word(sentence)
largest = largest_word(sentence)

print(f"The smallest and largest in the sentences is {smallest} and {largest} respectively.")