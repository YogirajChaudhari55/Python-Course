'''
File I/O can be used to store the generated data in a file to save it.
'''
filepath="file.txt"

f = open(filepath)
data = f.read()
print(data)
f.close()

