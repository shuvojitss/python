def fwrite(myname):
    try:
        f=open(myname,"w")
        while True:
            f.write(input("Write a line: "))
            f.write("\n")
            ch=input("Do u want to write again (y/n): ")
            if ch=='n' or ch=='N':
                break
        f.close()
    except IOError:
        print("File can not be created")
    return

fwrite("myname.txt")






#Write a line: my name is shuvojit
#Do u want to write again (y/n): n
