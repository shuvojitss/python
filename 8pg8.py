my_dict={'X':500,'Y':5874,'Z':560}
key_max=max(my_dict(),key=(lambda k:my_dict[key]))
key_min=min(my_dict(),key=(lambda k:my_dict[key]))
print('Maximum values=',key_max)
print('Minimum values=',key_min)

dict={'a':100,'b':200,'c':300}
key=input("Enter a key:")
if dict.has_key(key):
    print("Present value=",dict[key])
else:
    print("Not Present")


d1={6:'six'}
num.update(d1)
print(num)
del num[6]
print(num)
person={'name':'Phill','age':22,'salary':3500.00}
print('person=',person)
person={'name':'Phill','age':22}
print('Return Value=',result)

d={'a':100, 'b':200, 'c':300}
d.keys()
dict_keys(['a','b','c'])
d.items()
d={'a':100, 'b':200, 'c':300}
len(d)

sales={'apple':2,'orange':3,'grapes':4}
sales.pop(2)
print(sales)
