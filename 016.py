# 3値以上の最大公約数を求める
# 入力形式例
# 3
# 10 8 24
def gcd(a,b):
  if(a < 1):
    return b
  if(b < 1):
    return a
  if(a < b):
    return gcd(a, b % a)
  else:
    return gcd(b, a % b)

N = int(input())
L = list(map(int, input().split()))
print(gcd(L[0], L[1]))