import random


computer=random.choice([-1,1,0])
# print(computer)

you = input("Enter the choice:")

gameDict={"s":1, "w":-1, "g":0}
younum = gameDict[you]

if(computer == you):
    print("Game Tie")
else:
    if(computer-younum==2 or computer-younum==-1):
        print("Computer Wins")
    else:
        print("You win")