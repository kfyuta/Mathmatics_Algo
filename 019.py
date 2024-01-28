# 同じ色のカードの組み合わせ数
# 入力例
# 6
# 1 3 2 1 1 2

N = int(input())
L = list(map(int, input().split()))
M = {1:0,2:0,3:0}
for i in L:
  M[i] += 1
print(int(M[1]*(M[1]-1)/2 + M[2]*(M[2]-1)/2 + M[3]*(M[3]-1)/2))