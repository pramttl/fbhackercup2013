# Creating the memoize decorator.
def memo(f):
    cache = {}
    def memf(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf

from operator import mul
@memo
def nCr(n,r):
    if r > n-r:  # for smaller intermediate values
        r = n-r
    return int(reduce( mul, range((n-r+1), n+1), 1) / reduce( mul, range(1,r+1), 1) )


for t in xrange(int(raw_input())):
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    s = sorted(a)
    su = 0
    for i in xrange(k-1,n):
        su += s[i] * nCr(i,k-1)

    ans = su % 1000000007
    print "Case #%i:"%(t+1),ans
