# Write a Python program to find the second most repeated word in a given string.

from collections import Counter

def Second_most_repeated(text):
    word = text.split()
    freq = Counter(word)

    sorted_freq = sorted(freq.items(),key=lambda word:word[1],reverse=True)
    print(sorted_freq)
    if len(sorted_freq) < 2:
        return "No Repeated Words"
    return sorted_freq[1][0]

sentence = input("Enter the Sentence:- ")
print("The word with the second most repeated frequency is : - ", Second_most_repeated(sentence))
    


    
