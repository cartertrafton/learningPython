#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to teh start
# of each line of text in the clipboard

import pyperclip
text = pyperclip.paste()

#TODO: Seperate lines and add stars.

pyperclip.copy(text)
