words = 0
line_count = 0

with open("home.txt", 'r') as f:
    for line in f:
        w = line.split()
        words += len(w)
        line_count += 1

print("Total words:", words)
print("Total lines:", line_count)


#Total words: 11
#Total lines: 2


home.txt
I live in Howrah.
The city is beside the river Ganga.
