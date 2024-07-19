#The game() function in a program lets a user play a game and returns 
#the score as an integer. You need to read a file 'Hi-score.tt' which is 
# either blank or containes the provioud hi-score. You need to write a 
# program to update the Hi-score whenever the game() function breaks the 
# Hi-score.

import random



def game():
    print("Aaap Khel rahe hai")
    score = random.randint(0,100)
    print(f"Your Score is:{score}")
    #fetch the highscore
    with open("Hi-score.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

            
    if(score>hiscore or hiscore ==""):
        #write hiscore in the file
        with open("Hi-score.txt","w")as f:
            f.write(str(score))

    return score

game()
