def solution():
    
    answer =0
    
    # inf = open('input.txt');

    # n = inf.readline();
    n = input()
    
    n = int(n)    
    matchResult = [0]*(n*(n-1)) 
    team = [] 

    for i in range(n*(n-1)):
        matchResult[i]=input()
        # matchResult[i] = inf.readline();
        matchResult[i] = matchResult[i].split("\n")[0]
        
        #team 1
        already = 0
        for j in range(len(team)):
            if (matchResult[i].split(" ")[0] == team[j]["name"]): 
                already = 1 
                break
        if already == 0: 
            team.append({"name" :matchResult[i].split(" ")[0], "win" : 0, "lose" : 0 ,"plusMinus" : 0})
            
        #team2 
        already = 0        
        for j in range(len(team)):
            if (matchResult[i].split(" ")[2] == team[j]["name"]): 
                already = 1 
                break
        if already == 0: 
            team.append({"name" :matchResult[i].split(" ")[2], "win" : 0, "lose" : 0 ,"plusMinus" : 0})
        
        team1,score1,team2,score2 = matchResult[i].split(" ")
        score1 , score2 = int(score1), int(score2)

        if(score1 > score2):
            for j in range(len(team)):
                if team1== team[j]["name"]: 
                    team[j]["win"] = team[j]["win"]  + 1
                    team[j]["plusMinus"] = team[j]["plusMinus"] + score1 - score2                                        
            for j in range(len(team)):
                if team2== team[j]["name"]:
                    team[j]["lose"] = team[j]["lose"] + 1
                    team[j]["plusMinus"] = team[j]["plusMinus"] - (score1 - score2)
        else:
            for j in range(len(team)):
                if team1== team[j]["name"]: 
                    team[j]["lose"] = team[j]["lose"] + 1
                    team[j]["plusMinus"] = team[j]["plusMinus"] + score1 - score2       
            for j in range(len(team)):
                if team2== team[j]["name"]: 
                    team[j]["win"]  = team[j]["win"]  + 1
                    team[j]["plusMinus"] = team[j]["plusMinus"] - (score1 - score2)
                    
    newTeam = sorted(team, key=lambda k: k["name"]) 
    newTeam = sorted(newTeam, key=lambda k: k["plusMinus"],reverse = True) 
    newTeam = sorted(newTeam, key=lambda k: k['win'],reverse = True) 

    for i in range(n):
        print(newTeam[i]["name"]+" "+str(newTeam[i]["win"])+ " "+ str(newTeam[i]["plusMinus"]))
    return 

def main():
    solution()
    
main()