import os

#Specify the directory you want to list. Right now it selects C library
directory_path = '/'

#List all files and directory list
contents = os.listdir(directory_path)

#Print each file and directory name
for item in contents:
    print(item)