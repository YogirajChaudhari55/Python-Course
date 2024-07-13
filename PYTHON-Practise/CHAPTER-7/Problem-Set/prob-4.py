#Program to find whether a given number is prime or not

#Prime number only when that number is divsible by itself and 1 no by any other number

num=int(input("Enter a number: "))

for i in range(2,num):
    if(num%i==0):
        print("Not a prime number")
        break
else:
    print(f"{num} is a prime number")