import csv



# input nickname for the highscore
nickname = input('What is your nickname? This is for the highscore : ')

# Reads the highscore file and evaluates the dictionary to retrieve highscores
with open('highscore.txt','r') as csvfile:
    highscore = eval(csvfile.read())

# If nickname exits do not overwrite the their score
if nickname not in highscore:
    highscore[nickname] = 0
    # Writes in the new nickname
    with open('highscore.txt','w') as csvfile:
        csvfile.write('%s'%highscore)
else:
    print('Nickname already exist')