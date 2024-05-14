import numpy as np
def points(names,a):
    # !!! YOUR CODE HERE !!!
    return (a[:,:1]*3)+a[:,1:2]
def reportPoints(names,ptsTotal):
# !!! YOUR CODE HERE !!!
    ans=[]
    for i in range(len(names)):
        ans.append(names[i]+' '+str(ptsTotal[i][0]))
    return '\n'.join(ans)
#you can write your own tests too.
tableRows =np.array(["Win","Draw","Lose","GoalFor","GoalAgainst","match1","match2","match3","match4","match5"])
#test report Points
teamnames = np.array(["Newcastle", "Tottenham", "Brighton","Liverpool", "Leeds"])
table =np.array([[7,6,1,28,11,1,1,1,1,0],[8,2,4,27,18,0,1,0,0,1],[6,3,4,22,17,1,1,0,0,0],[5,4,4,25,16,1,0,0,1,1],[4,3,6,19,22,1,1,0,0,0]])
resPoints = points(teamnames,table)
resultPointsReport = reportPoints(teamnames,resPoints)
print(resPoints)
print()
print(resultPointsReport)