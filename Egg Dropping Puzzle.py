#Time Complexity: O(n*k^2)
#Auxiliary Space: O(n*k)
MAX=99999999
def EDP(eggs,floors):
    table=[[0 for i in range(floors+1)] for j in range(eggs+1)]
    for i in range(eggs+1):
        table[i][1]=1
    for i in range(floors+1):
        table[1][i]=i
    for i in range(2,eggs+1):
        for j in range(2,floors+1):
            table[i][j]=MAX
            for k in range(1,j+1):
                z=1+max(table[i-1][k-1],table[i][j-k])#max(the remaining numbers of eggs and the lower floors,total eggs and the above accessable floors)
                if(z<table[i][j]):#as we need the optimal value for the programm
                    table[i][j]=z

    return(table[eggs][floors])
                        
                    
    
t=int(input())
while(t>0):
    t=t-1
    n,floors=map(int,input().rstrip().rsplit())
    print(EDP(n,floors))
