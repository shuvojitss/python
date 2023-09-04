values = []
print("Enter 10 integers:")
for i in range(10):
    newValue = int(input("Enter integer %d:"%(i+1)))
    values+=[newValue]
print("\nCreating Histogram from values:")
print("%s %10s %10s" %("Element", "Value", "Histogram"))
for i in range(len(values)):
    print("%7d %10d %s" %(i, values[i],"*" * values[i]))
