def addnodes(n1, n2):
    nn = []
    nn.append(n1[0]+n2[0])
    bs = list(set(n1[1:] + n2[1:]))
    nn = nn + bs
    return nn

def bfline(times,l):
    n = len(times)
    if l == n -1 or l == 0:
        return None
    else:
        return l - 1

def optline(times, times_limit):
    n = len(times)
    ntimes = []
    for s in range(n):
        ntimes.append([])
        for e in range(n):
            bt = times[s][e]
            for p in range(n):
                #print(s, e, p)
                t = addnodes(times[s][p], times[p][e])
                if t[0] < bt[0] and len(t) >= len(bt):
                    bt = t
                elif t[0] <= bt[0] and len(t) > len(bt):
                    bt = t
                #elif (times_limit - t[0] >= 0 and len(t) > len(bt)):
                #    bt = t
            ntimes[s].append(bt)
    return ntimes


def optline2(times, times_limit):
    n = len(times)
    ntimes = []
    for s in range(n):
        ntimes.append([])
        for e in range(n):
            bt = times[s][e]
            for p in range(n):
                #print(s, e, p)
                t = addnodes(times[s][p], times[p][e])
                #if t[0] < bt[0] and len(t) >= len(bt):
                #    bt = t
                #elif t[0] <= bt[0] and len(t) > len(bt):
                #    bt = t
                if (times_limit - t[0] >= 0 and len(t) > len(bt)):
                    bt = t
            ntimes[s].append(bt)
    return ntimes
    
def transform(times):
    ntimes = [[0 for i in times] for j in times]
    n = len(times)
    for i in range(n):
        for j in range(n):
            ntimes[i][j] = [times[i][j], bfline(times, j)]
    return ntimes

def pl(l):
    for i in l:
        print(i)
    print(" ")

def solution(times, times_limit):
    n = 0
    nt = transform(times)
    pl(nt)
    gn = optline(nt, times_limit)

    for i in range(len(times)):
        nt = gn
        gn = optline(gn, times_limit)
        pl(nt)

    print("#########")

    while times_limit - gn[0][-1][0] >= 0 and n < len(times):
        nt = gn
        gn = optline2(gn, times_limit)
        pl(nt)
        n += 1
        print("n is" , n)
    
    g = nt[0][-1][1:]
    g.remove(None)
    return g

#print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))

#print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))

test = [[0, 3, 4, 6],
        [3, 0, 1, 7],
        [2, 3, 4, -2],
        [-3, 3, 4, 8]]

print(solution(test, 2))