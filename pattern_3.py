"""Write a code to generate a half pyramid number pattern.

Input Description:
Given an even integer R indicates number of rows.

Where 1<=R<=100.

Output Description:
Print the number half pyramid pattern with the size R.

Sample Input :
5
Sample Output :
12345
4321
123
21
1
"""

n=int(input())
k=0
for i in range(0,n):
  if(i%2==0):
    for j in range(1,n-k+1):
        print(j,end="")
  else:
      for p in range(n-k,0,-1):
        print(p,end="")
  k=k+1
  print()