fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

count = 0

fh = open(fname)
for line in fh:
    if not line.startswith ("From "):
        continue
    trying_to_split = line.split()
    print(trying_to_split[1])
    count = count+1

print("There were", count, "lines in the file with From as the first word")
