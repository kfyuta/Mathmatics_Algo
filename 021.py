def factrial(n):
    return 1 if n == 1 else (n * factrial(n-1))

def factrial_dec(n, i):
    a = 1
    j = 0
    while(j < i):
        a *= n
        j += 1
        n -= 1
    return a

def combination(n, r):
    return int(factrial_dec(n, r) / factrial(r))
