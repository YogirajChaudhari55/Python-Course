#Program to check if the given username contains less than 10 characters or not

username= input("Enter the username: ")

if(len(username) < 10):
    print("Correct username")
else:
    print("Incorrect username")