import heapq as hq

def put(d,e):
    try:
        d[e] += 1
    except KeyError:
        d[e] = 1

def rem(d,e):
    if d[e] == 1:
        del d[e]
    else:
        d[e] -= 1

for t in xrange(int(raw_input())):
    n, k = map(int,raw_input().split())
    a,b,c,r = map(int,raw_input().split())
    m = []
    m.append(a)
    for i in range(1,k):
        m.append((b * m[i - 1] + c) % r)

    d = {}
    for e in m:
        put(d,e)

    kset = set(range(k+1))
    remove_set = set(m[0:k])
    l = list(kset - remove_set)
    hq.heapify(l)

    j = (n-(k+1))%(k+1) + k
    for i in range(k,j+1):
        v = hq.heappop(l)
        m.append(v)
        put(d,v)
        rem(d,m[i-k])
        try:
            d[m[i-k]]
        except KeyError:
            hq.heappush(l,m[i-k])

    print "Case #%i:"%(t+1),m[j]

