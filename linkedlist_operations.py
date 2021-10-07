""""
Problem Statement:
Create an empty linked list.
You are given Q queries. Each query can be of the following types:

1. 1 x → insert number x to the end of the linked list
2. 2 → if the linked list size is > 0, then remove the first element
3. 3 x → remove all the occurrences of x in the linked list

Constraints
3 <= Q <= 1000
0 <= x <= 100000

Input Format
First-line contains a number Q.
Next Q lines contain 2 numbers type (can be either 1, 2 or 3) and x.

Output Format
Print the linked list

Sample Input 1
4
1 2
1 3
2
1 5

Sample Output 1
3 5

Explanation 1
After 1st operation, the linked list is 2
After 2nd operation, the linked list is 2 → 3
After 3rd operation, the linked list is 3
After 4th operation, the linked list is 3 → 5

Sample Input 2
4
1 3
1 3
1 5
3 3

Sample Output 2
5

Explanation 2
After 1st operation, the linked list is 3
After 2nd operation, the linked list is 3 → 3
After 3rd operation, the linked list is 3 → 3 → 5
After 4th operation, the linked list is 5
"""

linked_list=[]
for i in range(int(input())):
	
	s=list(map(int,input().split(" ")))
	if(s[0]==1):
		linked_list.append(s[1])
	elif(s[0]==2):
		if(len(linked_list)>0):
			linked_list.pop(0)
	elif(s[0]==3):
		while(s[0] in linked_list):
			linked_list.remove(s[1])
	s=[]
for i in linked_list:
	print(i,end=" ")