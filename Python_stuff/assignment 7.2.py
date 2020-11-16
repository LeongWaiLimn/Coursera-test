# Use the file name mbox-short.txt as the file name
user_input_fname = input("Enter file name: ")
fh = open(user_input_fname)

total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count+1
    #what is total count
    #print(count)

    #locate number
    #locate = line.find("0")
    #print(locate)

    #print(line.strip())

    value_of_srt = float(line[20:26])
    #print("The value is:", value_of_srt)
    #check if float works
    #print(type(value_of_srt))

	#calculate total

    total= total + value_of_srt
    #print("cl is", total)



print("Average spam confidence:",(total/count))
