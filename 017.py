# 3値以上の最小公倍数を求める
# 入力形式例
# 3
# 10 20 24

def gcd(a, b):
  while(a >= 1 and b >= 1):
    if(a < b):
      b = b % a
    else:
      a = a % b
  if(a >= 1):
    return a
  return b

def lcm(a,b):
  return int(a / gcd(a,b) * b)

N = int(input())
L = list(map(int, input().split()))
R = lcm(L[0], L[1])
for i in range(2, N):
  R = lcm(R, L[i])
  
print(R)