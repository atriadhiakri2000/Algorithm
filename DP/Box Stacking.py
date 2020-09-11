def maxHeight(height, width, length, n):

    rotate=[[0,0,0] for i in range(3*n)]

    j=0

    for i in range(n):

        rotate[j][0]=height[i]
        rotate[j][1]=max(width[i],length[i])
        rotate[j][2]=min(width[i],length[i])
        j=j+1

        rotate[j][0]=width[i]
        rotate[j][1]=max(height[i],length[i])
        rotate[j][2]=min(height[i],length[i])
        j=j+1

        rotate[j][0]=length[i]
        rotate[j][1]=max(width[i],height[i])
        rotate[j][2]=min(width[i],height[i])
        j=j+1

    rotate.sort(reverse = True)
    
    print(rotate)

    table=[0]*n*3
    
    for i in range(n*3):
        table[i]=rotate[i][0]

    for i in range(1,3*n):
        for j in range(0,i):
            if(rotate[i][1]<rotate[j][1] and rotate[i][2]<rotate[j][2]):
                if(table[i]<table[j]+rotate[i][0]):
                    table[i]=table[j]+rotate[i][0]

    m=-1
    m=max(max(table),m)
    
    print(table)

    return m
    
        
    


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        i=0
        height=[]
        width=[]
        length=[]
        for i in range(0,3*n,3):
            height.append(arr[i])
            width.append(arr[i+1])
            length.append(arr[i+2])
            
        print(maxHeight(height, width, length, n))
# Contributed bY: Harshit Sidhwa

# } Driver Code Ends
