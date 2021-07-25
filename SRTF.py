def arrange(dic):
    return dict(sorted(dic.items(), key=lambda e: e[1][0]))

def FastestProcess(dic, count):
    min = 100
    process = ""
    for i in dic:
        if dic[i][1] < min and dic[i][0] <= count:
            min = dic[i][1]
            process = i
    return process

def getTime(ps):
    time = 0
    for i in ps:
        time += ps[i][1] 
    return time
    
def WTAT(ps):
    import copy 
    psNew = copy.deepcopy(ps)
    time = getTime(ps)
    ct = ps[list(ps.keys())[0]][0]
    timeList = []
    for i in range(time):
        psNew = arrange(psNew)
        a = FastestProcess(psNew,ct)
        psNew[a][0]  += 1
        psNew[a][1]  -= 1
        timeList.append({a: ct})
        if psNew[a][1] == 0:
            del psNew[a]
        ct += 1
    return timeList

def DO(ps):
    timeList = WTAT(ps)
    cpu , check = [] , []
    for i in reversed(range(getTime(ps))):
        if list(timeList[i].items())[0][0] not in check:
            check.append(list(timeList[i].items())[0][0])
            cpu.append({list(timeList[i].items())[0][0]: list(timeList[i].items())[0][1]+1})
    return cpu

def avgTime(ps):
    cpu = DO(ps)
    waitingTimeList , turnAroundTimeList = [] , []
    avgWaitingTime , avgTurnAroundTime = 0 , 0

    for i in range(len(cpu)):
        x = list(cpu[i].items())[0][0] 
        waitingTimeList.append({x: list(cpu[i].items())[0][1] - ps[x][0] - ps[x][1]})
        turnAroundTimeList.append({x: list(cpu[i].items())[0][1] - ps[x][0]})
        avgWaitingTime += list(cpu[i].items())[0][1] - ps[x][0] - ps[x][1]
        avgTurnAroundTime += list(cpu[i].items())[0][1] - ps[x][0]

    avgWaitingTime /= len(cpu)
    avgTurnAroundTime /= len(cpu)
    return ps, waitingTimeList, turnAroundTimeList, avgWaitingTime, avgTurnAroundTime


