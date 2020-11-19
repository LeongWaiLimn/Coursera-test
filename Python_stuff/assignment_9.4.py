name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)



email_data = dict()
for readfile in handle:
    if not readfile.startswith ("From "):
        continue
    email_list = readfile.split()
    email_only = email_list[1]
    #print("Email list:",email_only)
    email_data[email_only]=email_data.get(email_only,0)+1

    email_count = None
    common_email = None

    for key,value in email_data.items():
        if email_count is None or value > email_count:
            common_email = key
            email_count = value




#print(email_data)
#print(email_data.items())
print(common_email,email_count)
