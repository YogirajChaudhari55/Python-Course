# Program to find the sum of first n natural numbers using the while loop

num=int(input("Enter a number: "))

i=1
sum=0

while(i<num+1):
    sum=sum+i
    i=i+1

print(sum)