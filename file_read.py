import os
f=open("pree.txt", "r")
if f.mode == 'r':
    contents =f.read()
    print(contents)