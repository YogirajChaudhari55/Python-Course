#Reapeat  program 4 for alist of words to be censored

words=["Donkey","bad","ganda"]

with open("donkey.txt") as f:
    d=f.read()
for word in words:
    d = d.replace(word,"#"* len(word))


with open("donkey.txt","w") as f:
    f.write(d)