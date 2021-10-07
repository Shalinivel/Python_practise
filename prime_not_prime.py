def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
re=[]
re1=[]
n=input()
arr=list(map(int,input().split(" ")))
print(arr)
for i in arr:
    if(test_prime(i)):
        re.append(str(i))
    else:
        re1.append(str(i))
re=re+re1
print(" ".join(re))
