f = open("file.txt")
data = f.read()
f.close()

#Same can be written with the with statement like this:

with open("file.txt") as f:
    print(f.read())

#using this you don't have close the file

