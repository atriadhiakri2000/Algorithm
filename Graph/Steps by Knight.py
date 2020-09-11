row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]

def valid(x,y,n):
    return not(x<0 or y<0 or x>=n or y>=n)

def ans(scr,dest,n):
    visited=[]
    q=[]
    q.append(scr)
    while(q):
        node=q.pop(0)
        print(node)
        if(node[0]==dest[0] and node[1]==dest[1]):
            return node[2]
        if(node not in visited):
            visited.append(node)
            for i in range(8):
                x=node[0]+row[i]
                y=node[1]+col[i]
                if valid(x,y,n):
                    q.append([x,y,node[2]+1])
            
    return float('inf')

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    scr=[x1,x2,0]
    dest=[x2,y2]
    print(ans(scr,dest,n))

'''
from collections import deque

def adj(s, n):
    adjl = []
    x = s[0]
    y = s[1]
    pal = [(x + 2, y - 1), (x + 2, y + 1), (x - 2, y + 1), (x - 2, y - 1), (x + 1, y + 2), (x - 1, y + 2),
           (x + 1, y - 2), (x - 1, y - 2)]

    for e in pal:
        if 0 < e[0] <= n and 0 < e[1] <= n:
            adjl.append(e)

    return adjl


def minstep(sxy, dxy, n):

    q = deque([sxy])
    minvstd = {(sxy): 0}

    if sxy == dxy:
        return 0

    while q:
        cn = q.popleft()

        for an in adj(cn, n):
            if an not in minvstd:
                if an == dxy:
                    return minvstd[cn] + 1

                minvstd[an] = minvstd[cn] + 1
                q.append(an)
            

    #return 1


if __name__ == '__main__':
    T=int(input())
    
    for tcs in range(T):
        n=int(input()) #size of board
        KnightXY=tuple(map(int, input().strip().split(' ')))
        targetXY=tuple(map(int, input().strip().split(' ')))
        
        print(minstep(KnightXY, targetXY, n))
'''
