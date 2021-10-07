"""
Problem Statement:
Given an array A of size N. Find the number of pairs (i,j) such that i<j and A[i]+A[j]=0

Constraints
3 <= N <= 100000
-100000 <= A[i] <= 100000

Input Format
First-line contains a number N.
Next line contains N space-separated numbers A[i].

Output Format
Print the number of such pairs

Sample Input 1
4
-1 -2 2 4

Sample Output 1
1

Explanation 1
2 and -2 is one such pair which sum to 0.

Sample Input 2
4
-2 -2 2 3

Sample Output 2
2

Explanation 2
(-2,2) and (-2,2) are 2 such pairs.
"""

n=input()
arr=list(map(int,input().split(" ")))
count=0
for i in range(len(arr)):
	for j in range(len(arr)):
		if(i<j):
			if(arr[i]+arr[j]==0):
				count+=1
				
print(count)

