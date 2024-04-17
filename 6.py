def getHoliday1(fname,month1): 
    f1 = open(fname)
    list1=[]
    for i in range(0,17,1):
        s1 = f1.readline().replace("\n","")
        str1="-"+str(month1).zfill(2)+"-"
        if str1 in s1:
            list1.append(s1)
    print(list1)
getHoliday1("holidays1.csv",3)
