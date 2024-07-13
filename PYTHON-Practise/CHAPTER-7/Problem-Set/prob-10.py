#Program to print the multiplication table of n using for loop in reversed manner

n=int(input("Enter the number: "))

for i in range(10,0,-1):
    print(f"{n} X {i} = {n*i}")
