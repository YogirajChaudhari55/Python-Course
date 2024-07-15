#Fcuntion to print first n lines of the following pattern:
'''
***
**
* for n =3
'''

n=int(input("Enter the number: "))

def pattern(n):
    for i in range(n,0,-1):
        print("*"*i)

pattern(n)
    