# Write a Python program to wrap a given string into a paragraph of given width.

import textwrap

def text_wrap(string,width):
    return textwrap.fill(string,width)

sentence = input("Enter the sentence:- ")
width = int(input("Enter the Width:- "))

print("Wrapped String:- \n", text_wrap(sentence, width))