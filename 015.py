# 3値以上の最大公約数を求める
def gcd(a,b):
  if(a < 1):
    return b
  if(b < 1):
    return a
  if(a < b):
    return gcd(a, b % a)
  else:
    return gcd(b, a % b)
  
L = list(map(int, input().split()))
print(gcd(L[0], L[1]))