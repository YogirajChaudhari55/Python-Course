#Recursive function to calculate the sum of first n natural numbers

n=int(input("Enter the number whose sum of naturals numbers you want to find: "))

'''
sum(5)=5 + 4 + 3 + 2 + 1 
sum(4)= 4+3+2+1
sum(5) = 5 + sum(4)
sum(n) = n + sum(n-1)
'''

def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

print(sum(n))

