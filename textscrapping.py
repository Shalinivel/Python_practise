message="CS_BT_21_7412@student.onlinedegree.iitm.ac.in"
message=message.split("@")
ins=message[1].split(".")

re=message[0].split("_")
for i in re:
    print(i)
print(ins[2])