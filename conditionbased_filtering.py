""""
Accept two positive integers M and N as input. There are two cases to consider:
(1) If M < N, then print M as output.
(2) If M >= N, subtract N from M. Call the difference M1. If M1 >= N, then subtract N from M1 and call the difference M2. Keep doing this operation until you reach a value k, such that, Mk <  N. You have to print the value of Mk as output. 
"""
m=int(input())
n=int(input())
if(m<n):
    print(m)
else:
    m1=m-n
    while(1 and m1>0):
        if(m1<n):
            break
        m1-=n
    print(m1)