def pibo(_n):
    if (_n <2):
        return _n
    return pibo(_n-2) + pibo(_n-1)

n=int(input())
print(pibo(n))
    