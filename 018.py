N = int(input())
L = list(map(int, input().split()))
M = {100:0,200:0,300:0,400:0} 
for i in L:
  if(i in M):
    M[i] += 1
print(M[100] * M[400] + M[200]*M[300])