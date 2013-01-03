t = int(raw_input())
for runs in xrange(t):
    d = int(raw_input())
    toSort = [int(x) for x in raw_input().split()]
    MAX = max(toSort)+2
    MAXN = len(toSort)+2
    ret = (len(toSort) * (len(toSort) - 1)) / 2
    c = []
    for x in range(MAX):
        c.append(0)
   
    for i in range(len(toSort)):
        j = toSort[i]
        while (j > 0):
            ret -= c[j]
            j -= j & -j
        
        j = toSort[i]
        while (j < MAX):
            c[j] += 1
            j += j & -j
    print( ret )