#Program to find out whether a file is identical and matches the content of another file

with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt") as f:
    content1 = f.read()

if(content == content1):
    print("the files are identical")
else:
    print("No Files are not identical")