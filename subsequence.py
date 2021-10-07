import collections
def PartitioningArray( A, k):

    if not A and k == 1:
        return("Yes")
    n = len(A)
    if k > n or n%k:
        return("No")
    groupnum = n//k
    cnt = collections.Counter(A)
    if groupnum < max(cnt.values()):
        return("No")
    else:
        return("Yes")

print(PartitioningArray([1,2,2,3],3))
    
