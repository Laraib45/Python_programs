"""
Share
Write a code to generate a inverted half pyramid pattern using numbers.

Input Description:
Given an integer R indicates number of rows.

Where 1<=R<=100

Output Description:
Print the number half pyramid pattern with the size R.

Sample Input :
5
Sample Output :
12345
1234
123
12
1
"""



n=int(input())
k=0
for i in range(0,n):
    for j in range(1,n-k+1):
        print(j,end="")
    k=k+1
    print()