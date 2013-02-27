def memoize(f):
    cache = {}
    def memf(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf


def alphastrip(os):
    s = ""
    n = len(os)
    for i in range(n):
        c = os[i]
        if c=='(' or c==')':
            s+=c
        if c ==':':
            try:            
                cp = os[i+1]
                if  cp == ':' or cp == ')' or cp == '(':
                    s+=c
            except IndexError:
                pass
    return s

def lstrip(s):
    broken = False
    for i in range(len(s)):
        if s[i] == '(':
            broken = True
            break
    if broken:
        if s[i-1] == ':':
            s = s[i-1:]
        else:
            s = s[i:]
        return s
    return s


def rstrip(s):
    broken = False
    for i in range(len(s)-1,-1,-1):
        if s[i] == ')':
            broken = True
            break
    if broken:
        return s[:i+1]
    return s

import re
def strip(s,cut = ':'):
    s = rstrip(lstrip(alphastrip(s)))
    ns = re.sub('\:+', ':', s)
    return ns

# Takes a pure paranthesis string.
def ponlychk(s):
    l = []
    for i in range(0,len(s)):
        c = s[i]
        if c=='(':
            l.append(c)
        elif c==')' and len(l) != 0 and l[-1]=='(':
            l.pop()
        else:
            return False
    if len(l) == 0:
        return True
    else:
        return False

@memoize
def check(s):
    i = s.find(':')
    if i == -1:
        return ponlychk(s)
    else:
        return check(s[:i] + s[i+1:]) or check(s[:i] + s[i+2:])



for t in xrange(int(raw_input())):
    s = raw_input()
    s = strip(s)
    c = check(s)
    if c:
        c = "YES"
    else:
        c = "NO"
    print "Case #%i:"%(t+1),c

