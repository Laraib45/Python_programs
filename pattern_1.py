"""Write a code to generate a half pyramid pattern using numbers.

Input Description:
Given an integer R indicates number of rows.

Where 1<=R<=100

Output Description:
Print the number half pyramid pattern with the size R.

Sample Input :
5
Sample Output :
5
45
345
2345
12345"""

n=int(input())
for i in range(0,n):
    for j in range(n-i,n+1):
        print(j,end="")
    print()

