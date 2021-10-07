def maxoccchar(text):
    max_l=-1
    text=list(text)
    for i in text:
        if(text.count(i)>max_l):
            max_l=text.count(i)
            string = i  
    return(string)
print(maxoccchar("bbbaaacc"))

