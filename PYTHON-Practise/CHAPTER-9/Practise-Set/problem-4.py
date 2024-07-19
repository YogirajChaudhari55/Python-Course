#A file containes a word"Donkey multiple times. You need to write a program which rplace this word with #### by updating the same file

word="Donkey"

with open("donkey.txt") as f:
    d=f.read()

if("Donkey" in d):
    e=d.replace("Donkey","#####")
    print(e)

with open("donkey.txt","w") as f:
    f.write(e)