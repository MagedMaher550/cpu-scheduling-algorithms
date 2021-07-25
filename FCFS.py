import operator
from itertools import islice

def arrange(PDic):
    return dict(sorted(islice(PDic.items(), 0, None), key=operator.itemgetter(1)))

# calculates the waiting time and turn around time for each process
def calcTime(Input):
    Input = arrange(Input)
    waitingTime , TurnArounTime = [] , []
    count = 0
    for i in Input:
        if int(Input[i][0]) > count:
            count = int(Input[i][0])
        waitingTime.append(count - int(Input[i][0]))
        TurnArounTime.append(count - int(Input[i][0]) + int(Input[i][1]))
        count += int(Input[i][1])

    return waitingTime , TurnArounTime

# calculates the average waiting time and the average turn around time
def calcAvgTime(Input):
    waitingTimeList = calcTime(Input)[0]
    TurnArounTimeList = calcTime(Input)[1]

    AvgWaitingTime, AvgTurnAroundTime = 0, 0
    for i in range(len(waitingTimeList)):
        AvgWaitingTime += waitingTimeList[i]
        AvgTurnAroundTime += TurnArounTimeList[i]
    avgWT = round(AvgWaitingTime/len(waitingTimeList),4) 
    avgTT = round(AvgTurnAroundTime/len(waitingTimeList) , 4)

    return Input , waitingTimeList , TurnArounTimeList, avgWT , avgTT