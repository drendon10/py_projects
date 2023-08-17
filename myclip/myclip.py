#This program copies text onto the clipboard but doesn't paste anything. One command line argument requiered


import pyperclip
import sys

TEXT = {'agree': """Yes I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this amonthly donation?"""}

if len(sys.argv) < 2:
    print("Usage: python myclip.py [keyphrase] - copy phrase text")
    sys.exit()

#First command line arg is the keyphrase
keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard")
else:
    print(f"There is no text for {keyphrase}")
