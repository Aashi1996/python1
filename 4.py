def getHoliday1(fname): 
    f1 = open(fname)
    list1=[]
    for i in range(0,17,1):
        s1 = f1.readline().replace("\n","")
        list1.append(s1)
    print(list1)
getHoliday1("holidays1.csv")
