def avg(x):
    summ=0
    for i in x:
        summ +=i
    average=summ/len(x)
    return average
def median(x):
    n=-1
    if((len(x)+1)%2)==0:
        n=int(len(x)/2)
    else:
        p=len(x)
        n=int(((p/2)+((p/2)+1))/2)
    return x[n]
def mode(x):
    c=1
    count=[]
    point=x[0]
    for i in range(1,len(x)):
        if x[i]==point:
            c+=1
        else:
            point=x[i]
            c=0
        count.append(c)
        maxx=max(count)
        i=count.index(maxx)
        return x[i]
s=input("Enter with spaces: ")
x=s.split()
c=0
for i in x:
    x[c]=int(i)
    c+=1
print(x)
x.sort()
print(x)
print(avg(x))
print(median(x))
print(mode(x))
