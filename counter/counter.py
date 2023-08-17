# Count the occurrences of a word in a given txt file

import string
import sys

# Check argv arguments
if len(sys.argv) != 3:
    sys.exit("Usage: counter.py (filename) (word to look for)")

path = sys.argv[1]
word_to_search = sys.argv[2]

# Open file and create a list of words using list comprehension
with open(path, 'r') as file:
    lines = file.readlines()
    words = [word for line in lines for word in line.split()]
    # Create a new list of the same words but without punctuation
    words_without_punctuation = [word2.translate(str.maketrans('', '', string.punctuation)) for word2 in words]
# Look for word in the list of words
counter = 0
for w in words_without_punctuation:
    if w.lower() == word_to_search.lower():
        counter += 1

print(f"'{word_to_search}' counter: {counter}")


