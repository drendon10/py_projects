# This program takes lines of text from your clipboard, adds a bulletpoint to them, and then gives it back to your clipboard to paste


import pyperclip
import sys

text = pyperclip.paste()

# Separate lines and add stars as bullet points
lines = text.split("\n")
# Adds a star to every item in the lines list
for i in range(len(lines)):
    lines[i] = f"* {lines[i]}"

# pyperclip.copy() is expecting a single string value not a list, join function will convert the list into a single string value
text = "\n".join(lines)
pyperclip.copy(text)

