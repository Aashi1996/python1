def getHoliday1(): 
    f1 = open("holidays1.csv")
    list1=[]
    for i in range(0,17,1):
        s1 = f1.readline().replace("\n","")
        list1.append(s1)
    print(list1)
getHoliday1()
