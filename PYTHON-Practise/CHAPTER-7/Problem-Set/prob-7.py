# Program to print pattern
 
# for n =3
''' 
  *
 ***
*****
'''

n=3

for i in range(1,n+1):
    print(" "*(n-i),end="") #does not add new line by default
    print("*"*(2*i-1))
    print("")


