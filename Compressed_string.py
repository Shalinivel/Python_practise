def compressedStr(message):
    stack=[]
    stack.append(message[0])
    res="" 
    for i in range(1,len(message)):
        if(stack[0]==message[i]):
            stack.append(message[i])
        else:
            res+=stack[0]+str(len(stack))
            stack=[]
            stack.append(message[i])
    if(len(stack)!=0):
        res+=stack[0]+str(len(stack))
    if(len(message)>len(message)):
        return(message)
    else:
        return(res)
print(compressedStr("abc"))