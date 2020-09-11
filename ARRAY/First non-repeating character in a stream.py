def print_first_nrc(q):
    
    for i in q:
        if i != -1:
            print(i, end=" ")
            return
    print("-1", end=" ")
t=int(input())
for _ in range(t):
    n = int(input())
    a = input().strip().split()
    cb = {}
    q = []
    nor = 0
    for i in range(n):
        cc = a[i]
        if cc not in cb:
            q.extend([cc])
            cb[cc] = [1, len(q)-1]
            print(q)
            print(cb)
        elif cb[cc][0] == 1:
            q[cb[cc][1]] = -1
            print(q)
        else:
            cb[cc][0] += 1

        print_first_nrc(q)
    print("")

