


import csv 


with open('highscore.txt', 'r') as csvfile:
    highscore = eval(csvfile.read())


nickname = input("Enter you're username for the highscore: ")

if nickname not in highscore:
        highscore[nickname] = 0
        # Writes in the new nickname
        with open('highscore.txt','w') as csvfile:
            csvfile.write('%s'%highscore)