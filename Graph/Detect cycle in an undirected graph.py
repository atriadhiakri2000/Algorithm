def isCyclic(g,n):
    visited=[False]*n
    for i in range(n):
        if(visited[i]==False):
            if(chkcyclic(g,visited,i,-1))==True:
                return True
    return False

def chkcyclic(g,visited,i,parent):
    visited[i]=True
    for j in g[i]:
        if(visited[j]==False):
            if(chkcyclic(g,visited,j,i)==True):
                return True
        elif(parent!=j):
            return True
    return False
