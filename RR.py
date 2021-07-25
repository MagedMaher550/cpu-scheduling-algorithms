def arrange(PDic):
    return dict(sorted(PDic.items(), key=lambda e: e[1][0]))

# calculates the time each process got to the cpu
def cpuCalc(Input, qt):
    import copy
    ps = copy.deepcopy(Input)
    cpuStack = []

    for i in range(len(ps)):
        count = 0
        k = i
        del ps
        ps = copy.deepcopy(Input)

        for j in range(100):
            if ps[j][2] > qt:
                count += qt
                ps[j][2] -= qt
                ps.append([ps[j][0],count,ps[j][2]])
                ps.sort(key=lambda x:x[1])

            else:
                count += ps[j][2]
                if ps[j][0] == k: 
                    cpuStack.append(count)
                    break
    return cpuStack

def wTime(Input, qt):
    cpuStack , waitingTimeList , turnAroundTimeList= cpuCalc(Input, qt) , [] , []
    avgWaitingTime , avgTurnAroundTime = 0 , 0
    for i in range(len(cpuStack)):
        waitingTimeList.append(cpuStack[i] - Input[i][1] - Input[i][2])
        turnAroundTimeList.append(cpuStack[i] - Input[i][1])
        avgWaitingTime += cpuStack[i] - Input[i][1] - Input[i][2]
        avgTurnAroundTime += cpuStack[i] - Input[i][1]

    avgWaitingTime /= len(cpuStack)
    avgTurnAroundTime /= len(cpuStack)
    return Input, cpuStack, waitingTimeList, turnAroundTimeList, avgWaitingTime, avgTurnAroundTime