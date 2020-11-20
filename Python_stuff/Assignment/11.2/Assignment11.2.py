import re

enter_file = input("Please enter file name:")
if len(enter_file)>1 : enter_file = "regex_sum_1072175.txt"
handle = open(enter_file)

count = 0
templist = list()
new_list_value = list()
for readfile in handle:
    cleanfile = readfile.strip()
    numbers_only = re.findall ('[0-9]+',cleanfile)
    if numbers_only is None or numbers_only == []: continue
    #check number string
    #print(numbers_only)
    #check type
    #print(type(numbers_only))
    for STRnumbers in numbers_only:
        templist.append(numbers_only)
        count = count + 1
        #check STRnumbers
        #print(STRnumbers)
        #check type
        #print(type(STRnumbers))
        value_only = int(STRnumbers)
        #check value
        #print(value_only)
        #check type
        #print(type(value_only))
        new_list_value.append(value_only)

#print("list of numbers:",templist)
print("Number count is:",count)
print("Total sum is:", sum(new_list_value))
