f = open("mynamet.txt", "a")
f.write("Now the file has more content!")
f.close() #open and read the file after the appending:
f = open("myname.txt", "r")
print(f.read())


#Hello! Welcome to demofile.txt.
#This file is for testing purposes.
#Good Luck!
#Now the file has more content!
