"""
Problem Statement – Ratan is a crazy rich person. And he is blessed with luck, so he always made the best profit possible with the shares he bought. That means he bought a share at a low price and sold it at a high price to maximize his profit. Now you are an income tax officer and you need to calculate the profit he made with the given values of stock prices each day. You have to calculate only the maximum profit Ratan earned.

Note that:

Ratan never goes into loss.
 

Example 1

Price=[1,6,2]
Ratan buys it on the first day and sells it on the second. 
Example 2

Price=[9,8,6] 
The Price always went down, Ratan never bought it.

 

Input Format:

First line with an integer n, denoting the number days with the value of the stack
Next n days, telling the price of the stock on that very day.
 

Output Format:

Maximum profit done by Ratan in a single line.
 

Constraints:

Number of days <=10^8

"""


def maxprofit(arr):
    max_stack=[0]
    min_stack=[]
    min_stack.append(arr[0])
    current_max=0
   
    for i in range(1,len(arr)):
        min_stack[0]=min(arr[i],min_stack[0])
        temp=arr[i]-min_stack[0]
        if(temp>current_max):
            current_max=temp
            max_stack[0]=arr[i]
    return(current_max)

print(maxprofit([1,9,2,11,1,9,2]))
