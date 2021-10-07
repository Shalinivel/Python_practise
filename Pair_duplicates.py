def winner(erica,bob):
    res={"E":1,"H":5,"M":3}
    escore=0
    bscore=0
    for i in erica:
        escore+=res[i]
    for i in bob:
        bscore+=res[i]
    if(escore>bscore):
        return("Erica")
    elif (bscore>escore):
        return("Bob")
    else:
        return("Tie")
print(winner("EEH","HHE"))