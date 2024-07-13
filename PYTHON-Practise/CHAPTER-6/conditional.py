#these statement have conditons in themand will be iimplemented only when there is fulfilment of condtion
# This is if-elif-else ladder. You can write seperate if, else as well.
a=int(input("Enter your age:"))

if(a>18):
    print("You are above the age of consent")

elif(a<0):
    print("Ypu are entering an invalid age.")

elif(a==0):
    print("You are entering 0 which is an invalid age.")

else:
    print("Below the age of concent")

print("End of program")