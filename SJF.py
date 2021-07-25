import operator
from itertools import islice

def arrange(PDic):
    return dict(sorted(islice(PDic.items(), 0, None), key=operator.itemgetter(1)))

#finds the process with least burst time
def FastestProcess(dic, count):
    min = 100
    process = ""
    for i in dic:
        if dic[i][1] < min and dic[i][0] <= count:
            min = dic[i][1]
            process = i
    return process


#calculates the time each process got to the cpu
def cpuCalc(Input):
    import copy    
    dic = arrange(copy.deepcopy(Input))
    firstProcess = list(dic.keys())[0]
    CPU = {
        firstProcess: dic[firstProcess][0]
    }
    count = dic[firstProcess][1]
    del dic[firstProcess]
    while len(dic) != 0 :
        a = FastestProcess(dic, count)
        if count < dic[a][0]:
            count = dic[a][0]
        CPU[a] = count
        count += dic[a][1]
        del dic[a]
    return dict(sorted(CPU.items()))

# calculates the waiting time and turn around time for each process
def calcTime(Input):
    CPU = cpuCalc(Input)
    T_Dic = {}
    for i in Input:
        x = CPU[i] - Input[i][0]
        T_Dic[i] = {
            "WaitingTime": x ,
            "TurnAroundTime": x + Input[i][1]
        }
    return T_Dic

# calculates the average waiting time and the average turn around time
def calcAvgTime(Input):
    dic = calcTime(Input)
    AvgWaitingTime, AvgTurnAroundTime = 0, 0
    for i in dic:
        AvgWaitingTime += dic[i]["WaitingTime"]
        AvgTurnAroundTime += dic[i]["TurnAroundTime"]
    return Input, dic ,round(AvgWaitingTime/len(dic),4), round(AvgTurnAroundTime/len(dic) , 4)
