# Nを素因数分解する
N = int(input())
# 繰り返しの上限。対象の数の√まで繰り返せばよい
L = int(N ** 0.5)
A = []
for i in range(2, L + 1):
  while N % i == 0:
    A.append(i)
    N /= i

# 最後に√N以上の余りが出た場合、その数も素因数のため追加
if N >= 2:
  A.append(int(N))

print(*A)