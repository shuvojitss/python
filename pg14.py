playList=[]
for i in range(5):
    playName=input("Play %d: "%(1+i))
    playList.append(playName)
print("\nSubscript value")
for i in range(len(playList)):
    print("%9d %-25s" %(i+1,playList[i]))
