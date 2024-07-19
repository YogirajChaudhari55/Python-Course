#Program to read the text from a given file 'poem.txt and find out whether it contains the word "twinkle".

with open("poems.txt") as f:
    d=f.read()
print(d)

if(d.find("Twinkle")>=0):
    print("It contians Twinkle")
else:
    print("It does not contain Twinkle")

