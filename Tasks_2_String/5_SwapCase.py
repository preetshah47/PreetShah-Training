# Write a Python program to swap cases of a given string.

def swap_case(string):
    return string.swapcase()

sentence = input("Enter the Sentence:- ")

result = swap_case(sentence)
print(f"Given String :- {sentence} \n Swap String :- {result}")
