def maxSubstrings(s):
    res=[s[i:j] for  i in range(len(s)) for j in range(i+1,len(s)+1)]
    res.sort()
    return(res[-1])



print(maxSubstrings("aaa"))