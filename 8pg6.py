a=set((1,2,3,4,7,9))
b=set((1,3,5,7,9))
print(a|b)
print(a&b)
print(a-b)
print(a^b)

def comp(n):
    for i in range(2,n):
        if n%i==0:
            return True
        return False
a={x for x in range(1,11) if x%2==0}
b=[x for x in range(1,21)]
b=set(list(filter(comp,b)))
a.add(0)
print(a)
print(a.issuperset(b))
print(len(a))

d1={'a':1,'b':2,'c':3}
d2={}
print(d1)
for key in d1:
    d2[d1[key]]=key
print(d2)

d={}
d2={}
for i in range(3):
    x=input("Enter name:")
    y=input("Enter ID:")
    z=list(map(str,input("Enter products sold:").split()))
    d['name']=x
    d['ID']=y
    d['products']=z
    d2a[i+1]=d
print(d2)
