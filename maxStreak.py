def maxStrek(m,data):
    res=0
    c=0
    for i in data:
        if "N" not in i:
            c+=1
        else:
            res=max(c,res)
            c=0
    res=max(c,res)
    return(res)
    
print(maxStrek(4,["YYY","YYY","YNN","YYN","YYN"]))
print(maxStrek(2,["YN","NN"]))