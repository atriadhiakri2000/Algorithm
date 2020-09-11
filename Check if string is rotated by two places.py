t=int(input())
while(t>0):
    t=t-1
    s=input()
    s2=input()
    if ((s[2:] + s[0:2]==s2) or (s[-2:] + s[0:-2] == s2)): # print(n1[2:] + n1[0:2]) print(n1[-2:] + n1[0:-2])
        print(1)
    else:
        print(0)
        
