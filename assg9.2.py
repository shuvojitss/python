def changeme(mylist):
    mylist.append([1,2,3,4])
    print("Values inside the function:",mylist)
    return
mylist=[10,20,30]
changeme(mylist);
print("Values outside the function",mylist)

x=int(input("Enter number:"))
product=1;
def fact(x):
    pro=1
    for i in range(1,x+1):
        pro *=i
    return pro
def factrec(x):
    product=1
    if x==1:
        return 1
    product=product *x*factrec(x-1)
    return product
product=factrec(x)
print(product)
