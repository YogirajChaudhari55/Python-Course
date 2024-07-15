'''
1 FOR SNAKE
-1 FOR WATER
0 FOR GUN
'''
import random


computer=random.choice([-1,1,0])
# print(computer)

you = input("Enter the choice:")

gameDict={"s":1, "w":-1, "g":0}
younum = gameDict[you]

if(computer==1 and younum==-1):
    print("Computer won")

elif(computer==1 and younum==0):
    print("You won")

elif(computer==-1 and younum==1):
    print("You won")

elif(computer==-1 and younum==0):
    print("Computer won")

elif(computer==0 and younum==1):
    print("Computer won")

elif(computer==0 and younum==-1):
    print("You won")

else:
    print("Results Tie")


