def hiever(myList):
    for name in myList:
        print("Hi,", name)

hiever(["Adam","John","Lucy"])

def crealist(n):
    myList=[]
    for i in range(n):
        myList.append(i)
    return myList
print(crealist(8))
