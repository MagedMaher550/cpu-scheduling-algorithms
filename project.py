from tkinter import *

import FCFS
import SJF
import SRTF
import RR


window = Tk()
window.title("Statistical Model")
window.configure(background="#f1f1f1")
window.geometry("600x400+300-200")

#Get the number of processes
Label (window, text="Enter The Number Of Processes: ", bg="#f3f3f3", fg="black", font="none 12 bold").grid(row=1, column=1, sticky=W, pady=10)
NumberOfProcesses = Entry(window, width=20, bg="#FFF")
NumberOfProcesses.grid(row=1, column=2, sticky=W)

#Get the method name
Label (window, text="Enter The Name Of The Method: ", bg="#f3f3f3", fg="black", font="none 12 bold").grid(row=2, column=1, sticky=W)
Label (window, text="Methods Are: FCFS, SJF, SRTF , RR or ALL ", bg="#f1f1f1", fg="#F3823C", font="none 10 bold").grid(row=3, column=1, sticky=W)
MethodName = Entry(window, width=20, bg="#FFF")
MethodName.grid(row=2, column=2, sticky=W)

def isNumeric(n):
    check = True
    try:
        n = int(n)
    except:
        check = False
    return check

AT , BT = [] , []
processes = {}

def Open(n , MethodName):
    from tkinter import messagebox

    if (MethodName != "FCFS" and MethodName != "SJF" and MethodName != "SRTF" and MethodName != "RR" and MethodName != "ALL"):
        messagebox.showwarning("Invalid Data", "Please Enter a Valid Method Name")
    elif not isNumeric(n):
        messagebox.showwarning("Invalid Data", "Please Enter a Valid Number Of Processes")
    else:     
        n = int(n)
        if n <= 0:
            messagebox.showwarning("Invalid Data", "Please Enter a Valid Number Of Processes")
        else:
            en1 , en2 = [] , []
            n = int(n)
            DataWindow = Toplevel()
            DataWindow.title("Getting Data")
            DataWindow.configure(background="#f1f1f1")
            DataWindow.geometry("600x500+150-200")   

            def randString():
                import random 
                alpha , res = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" , ""
                for i in range(int(random.random()*100)):
                    res += alpha[int(random.random()*len(alpha))]
                return res

            for i in range(n):
                vaa = randString()
                va = randString()

                Label (DataWindow, text="P" + str(i+1), bg="#f3f3f3", fg="black", font="none 12 bold").grid(row=i+2, column=1, sticky=W, pady=10)
                vaa = Entry(DataWindow, width=10, bg="#FFF")
                vaa.grid(row=i+2, column=2 , pady=5 , padx=(0,10))

                va = Entry(DataWindow, width=10, bg="#FFF")
                va.grid(row=i+2, column=3 , pady=5)

                en1.append(vaa)
                en2.append(va)

            if MethodName == "RR" or MethodName == "ALL":
                Label (DataWindow, text="QT: ", bg="#f3f3f3", fg="black", font="none 12 bold").grid(row=n+2, column=1, sticky=W, pady=10)
                qt = Entry(DataWindow, width=10, bg="#FFF")
                qt.grid(row=n+2, column=2)

            def saveData():
                for i in en1:
                    AT.append(int(i.get()))
                for j in en2:
                    BT.append(int(j.get()))

                for i in range(n):
                    processes["p" + str(i + 1)] = [AT[i],BT[i]]

                def Result():
                    ResultWindow = Tk()
                    ResultWindow.title("FCFS Calculations Result")
                    ResultWindow.configure(background="#f1f1f1")
                    ResultWindow.geometry("900x500+150-200")

                    res = FCFS.calcAvgTime(processes)
                    Input = res[0]
                    WaitingTimeList = res[1]
                    TurnArounTimeList = res[2]
                    avgWT = res[3]
                    avgTT = res[4]

                    Header = " "*10 + "Arrival Time" + " "*5 + "Burst Time" + " "*5 + "Waiting Time" + " "*5 + "Turn Around Time"
                    Label(ResultWindow,text=Header, bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=1, column=1, sticky=W, pady=10)

                    for i in range(len(Input)):
                        show = "P" + str(i+1) + " "*(5+len("Arrival Time")) + str(Input[list(Input.keys())[i]][0]) + " "*(7+len("Brust Time")) + str(Input[list(Input.keys())[i]][1]) + " "*(10+len("Waiting Time")) + str(WaitingTimeList[i]) + " "*(13+len("Turn Around Time")) + str(TurnArounTimeList[i])                        
                        Label(ResultWindow,text=show, bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=i+2, column=1, sticky=W, pady=10)

                    Label(ResultWindow,text="Average Waiting Time = " + str(avgWT) + "  &&  " + "Average Turn Around Time = " + str(avgTT), bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=n+4, column=1, sticky=W, pady=107)
                def calcSJF():
                    ResultWindow = Tk()
                    ResultWindow.title("SJF Calculations Result")
                    ResultWindow.configure(background="#f1f1f1")
                    ResultWindow.geometry("900x500+150-200")

                    # return Input, dic ,round(AvgWaitingTime/len(dic),4), round(AvgTurnAroundTime/len(dic) , 4)
                    res = SJF.calcAvgTime(processes)
                    Input = res[0]
                    cpu = res[1]
                    avgWT = res[2]
                    avgTT = res[3]

                    Header = " "*10 + "Arrival Time" + " "*5 + "Burst Time" + " "*5 + "Waiting Time" + " "*5 + "Turn Around Time"
                    Label(ResultWindow,text=Header, bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=1, column=1, sticky=W, pady=10)

                    show = ""
                    w = 0
                    for i in cpu:
                        show = str(i).capitalize() + " "*10 + str(Input[i][0]) + " "*(len("Arrival Time")+10) + str(Input[i][1]) + " "*(len("Burst Time")+15) + str(cpu[i]["WaitingTime"]) + " "*(len("WaitingTime")+15) +str(cpu[i]["TurnAroundTime"])
                        Label(ResultWindow,text=show, bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=w+2, column=1, sticky=W, pady=10)
                        w += 1
                            
                    Label(ResultWindow,text="Average Waiting Time = " + str(avgWT) + "  &&  " + "Average Turn Around Time = " + str(avgTT), bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=n+4, column=1, sticky=W, pady=107)
                def calcSRTF():
                    DataWindow = Toplevel()
                    DataWindow.title("SRTF Calculations Result")
                    DataWindow.configure(background="#f1f1f1")
                    DataWindow.geometry("900x500+150-200")
                        
                    AT , BT = [] , []    
                    ps = {}
                    for i in en1:
                        AT.append(int(i.get()))
                    for j in en2:
                        BT.append(int(j.get()))

                    for i in range(n):
                        ps["p" + str(i + 1)] = [AT[i],BT[i]]

                    res = SRTF.avgTime(ps)
                    avgWt = res[3]
                    avgTt = res[4]
                    wtList = res[1]
                    TatList = res[2]
                    Input = res[0]

                    Header = " "*10 + "Arrival Time" + " "*5 + "Burst Time" + " "*5 + "Waiting Time" + " "*5 + "Turn Around Time"
                    Label(DataWindow,text=Header, bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=1, column=1, sticky=W, pady=10)

                    wtList.reverse()
                    TatList.reverse()
                    for i in range(len(wtList)):
                        value = list(wtList[i].items())[0][1]
                        tValue = list(TatList[i].items())[0][1]
                        key = list(wtList[i].items())[0][0]

                        show = key + " "*(5+len("Arrival Time")) + str(Input[key][0]) + " "*(7+len("Brust Time")) + str(Input[key][1]) + " "*(10+len("Waiting Time")) + str(value) + " "*(13+len("Turn Around Time")) + str(tValue)
                        Label(DataWindow,text=show, bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=i+2, column=1, sticky=W, pady=10)

                    Label(DataWindow,text="Average Waiting Time = " + str(round(avgWt,4)) + " && " + "Average Turn Around Time = " + str(round(avgTt,4)), bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=n+4, column=1, sticky=W, pady=107)

                def calcRR():
                    DataWindow = Toplevel()
                    DataWindow.title("RR Calculations Result")
                    DataWindow.configure(background="#f1f1f1")
                    DataWindow.geometry("900x500+150-200")   
                        
                    AT , BT = [] , []    
                    ps = []
                    for i in en1:
                        AT.append(int(i.get()))
                    for j in en2:
                        BT.append(int(j.get()))

                    for i in range(n):
                        ps.append([i,AT[i],BT[i]])

                    res = RR.wTime(ps,int(qt.get()))
                    avgWt = res[4]
                    avgTt = res[5]
                    wtList = res[2]
                    TatList = res[3]
                    Input = res[0]

                    Header = " "*10 + "Arrival Time" + " "*5 + "Burst Time" + " "*5 + "Waiting Time" + " "*5 + "Turn Around Time"
                    Label(DataWindow,text=Header, bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=1, column=1, sticky=W, pady=10)

                    w = 0
                    for i in range(len(Input)):
                        show = "P" + str(i+1) + " "*10 + str(Input[i][1]) + " "*(len("Arrival Time")+10) + str(Input[i][2]) + " "*(len("Burst Time")+15) + str(wtList[i]) + " "*(len("WaitingTime")+15) +str(TatList[i])
                        Label(DataWindow,text=show, bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=w+2, column=1, sticky=W, pady=10)
                        w += 1
                    Label(DataWindow,text="Average Waiting Time = " + str(round(avgWt,4)) + " && " + "Average Turn Around Time = " + str(round(avgTt,4)), bg="#f1f1f1", fg="black", font="none 15 bold").grid(row=n+4, column=1, sticky=W, pady=107)

                if MethodName == "FCFS":
                    Result()
                elif MethodName == "SJF":
                    calcSJF()
                elif MethodName == "SRTF":
                    calcSRTF()
                elif MethodName == "RR":
                    calcRR()
                else:
                    calcSRTF()
                    calcRR()
                    calcSJF()
                    Result()
        
            Button(DataWindow, text="Enter Data", width=10, command=saveData).grid(row=n+3, column=1, pady=5, sticky=W)


Button(window, text="Enter Data" , width=6 , command= lambda:Open(NumberOfProcesses.get(),MethodName.get())).grid(row=4, column=1, pady=5, sticky=W)

text = StringVar()
text.set("")
Label(window, textvariable=text, bg="#f3f3f3", fg="black", font="none 12 bold").grid(row=7, column=2, sticky=W)

mainloop()