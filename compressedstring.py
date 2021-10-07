def scompressedString(message):
    comp_str = ""
    count = 1
    for i in range(len(message)-1):
        if message[i] == message[i+1]:
            count += 1
        else:
            comp_str += message[i] + str(count)
            count = 1
    comp_str += message[i] + str(count)

    if len(comp_str) >= len(message):
        return message
    else:
        res=""
        for i in comp_str:
            if(i=="1"):
                pass
            else:
                res+=i
        return(res)


    
input_str_test_2 ="aaaaaabbccbcaabb"
print(scompressedString(input_str_test_2))
