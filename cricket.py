def play (name):
    

    teamAScore =0 #total runs score
    teamABalls =20 # number of balls remaining
    teamABalls_static =20 #balls for controlling a loop
    teamAWicket =0 # number of wickets taken
    


    print(f"\n=== {name} ====\n")
    for i in range(teamABalls_static):
        shot = input(f"Score : {teamAScore} / Out : {teamAWicket} - Balls {teamABalls} : ") #shot variable asks users to give input for (runs or out)
        if(teamAWicket==10):
            break
        if(shot.lower() == "o" or shot.lower() == "out"):
            teamABalls -=1
            teamAWicket+=1
            print("Player Out !")
        elif (int(shot)<0 or int (shot)>6):
            print("0-6 runs allowed")
        else:
            teamABalls -=1
            run = int(shot)
            teamAScore += run
    return teamAScore

# save returned scores 
teamAScore=play("Team A")
teamBScore=play("Team B")

# compare and determine the winner
if(teamAScore>teamBScore):
    print("Team A Wins")
elif(teamAScore<teamBScore):   
    print("Team B Wins")
else:
    print("Draw")