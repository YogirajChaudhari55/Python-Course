#Python program to rename a file to "renamed_by_python.txt"

with open("this.txt") as f:
    content = f.read()

with open("this_renamed.txt","w") as f:
    f.write(content)