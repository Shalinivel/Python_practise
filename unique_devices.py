def deviceNamesytem(devicenames):
    dico={}
    result=[]

    for item in devicenames:
        if item in dico.keys():
            dico[item]+=1
            result.append(f"{item}{dico[item]}")
        else:
            dico[item]=0
            result.append(f"{item}")
    return(result)
print(deviceNamesytem(["tv","remote","tv","tv","remote","cell"]))
