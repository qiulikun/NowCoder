import sys
N = input()
maxp = 0
bestm = 0

def mind(pos, m):
    l = len(pos)
    mindis = l
    for i in range(l):
        if pos[i] == 1 and abs(i-m) < mindis:
            mindis = abs(i-m)
    return -1 if mindis in [1,l] else mindis

def goodm(pos):
    l = len(pos)
    maxdis = 1
    goodi = -1
    for i in range(l):
        if pos[i] == 0:
            mindis = mind(pos, i)
            if mindis > maxdis:
                maxdis = mindis
                goodi = i
    return goodi

def gogo(pos, m):
    nextm = m
    p = 0
    while nextm != -1:
        import sys
N = input()
maxp = 0
bestm = 0

def mind(pos, m):
    l = len(pos)
    mindis = l
    for i in range(l):
        if pos[i] == 1 and abs(i-m) < mindis:
            mindis = abs(i-m)
    return -1 if mindis in [1,l] else mindis

def goodm(pos):
    l = len(pos)
    maxdis = 1
    goodi = -1
    for i in range(l):
        if pos[i] == 0:
            mindis = mind(pos, i)
            if mindis > maxdis:
                maxdis = mindis
                goodi = i
    return goodi

def gogo(pos, m):
    nextm = m
    p = 0
    while nextm != -1:
        pos[nextm] = 1
        nextm = goodm(pos)
        p += 1
    return p

for m in range(N):
    pos = [0]*N
    p = gogo(pos, m)
    if p > maxp:
        maxp = p
        bestm = m
print maxp, bestm+1
        nextm = goodm(pos)
        p += 1
    return p

for m in range(N):
    pos = [0]*N
    p = gogo(pos, m)
    if p > maxp:
        maxp = p
        bestm = m
print maxp, bestm+1
