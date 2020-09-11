import sys
sys.setrecursionlimit(100000)

def chk(matrix,table,i,j,n,m):
    return(i>=0 and i<n and j>=0 and j<m and not table[i][j] and
           matrix[i][j])
    
def DFS(matrix,table,i,j,n,m,count):
    table[i][j]=True
    row = [-1, -1, -1,  0, 0,  1, 1, 1]
    col = [-1,  0,  1, -1, 1, -1, 0, 1]
    for k in range(8):
        if(chk(matrix,table,i+row[k],j+col[k],n,m)):
            count[0]=count[0]+1
            DFS(matrix,table,i+row[k],j+col[k],n,m,count)

def findMaxArea(n,m,matrix):
    table=[[False for j in range(m)] for i in range(n)]
    result=-9999999999999
    for i in  range(n):
        for j in range(m):
            if(table[i][j]==False and matrix[i][j]==1):
                count=[1]
                DFS(matrix,table,i,j,n,m,count)
                result=max(result,count[0])
    return result
