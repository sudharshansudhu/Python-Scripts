from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename( filetypes =  ( ("Text files","*.txt"),("All files","*.*") ) )

print(root.filename)

f = open(root.filename)
lines = 0
words = 0
text = ''

for line in f:
    text = text+line
    lines = lines+1


for c in text:
    if (c==' ' or c=='\t' or c=='\n'):
        words = words+1
print("Number of lines are "+str(lines))
print("Number of letters are "+str(len(text)))
print("Number of words are "+str(words))

