num={1:'One', 2:'two', 3:'three', 4:'four', 5:'five'}
num.clear()
print(num)

d={i:i**3 for i in range(1,10)}
print(d)

d={i:i**3 for i in range(1,10,2)}
print(d)



d1={1:100,2:200,3:300}
d2={4:400,5:500}
d1.update(d2)
print(d1)

pyDict={'e':1,}





pyFSet=frozenset(('e','a','i','o','u'))
print(sorted(pyFSet,reverse=True))

statesAndCapitals={'Gujrat':'Gandhinagar','Maharashtra':'Mumbai','Rajasthan':'Jaipur'}
print('List Of given States:\n')
for state in statesAndCapitals:
    print(state)

keys=['red','green','blue']
values=['#FF0000','#008000','#0000FF']
color_dictionary=dict(zip(keys,values))
print(color_dictionary)


