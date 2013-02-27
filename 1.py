T = int(raw_input())
for t in xrange(T):
    s = raw_input().lower()
    d = {}
    for c in s:
        asc = ord(c)
        if asc>96 and asc<123:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

    l = sorted(d,key=d.get)
    l.reverse()
    b = 26
    s = 0
    for c in l:
        s += d[c] * b
        b -= 1
    print "Case #%i:"%(t+1),s
