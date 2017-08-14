"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SPECIAL = "!@#$%^&*()_+"

# word_format = "ccvcvvc"
word_format = input("Please enter word format (c for Consonants, v for Vowels and s for Specials): ".lower())
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    elif kind == "v":
        word += random.choice(VOWELS)
    else:
        word += random.choice(SPECIAL)

print(word)
