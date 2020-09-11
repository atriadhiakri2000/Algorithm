#code
def solve(arr,n):
    table=[2]*n #DP table with 2 for every element
    val=2 #Coz the minimun length of the AP has to be 2
    if(n<=2):
        print(n)
    else:
        arr.sort()
        for i in range(n-2,-1,-1): #Travese the list in the opposite direction leaving the first two elements as the min no of elements needed for the AP is 2
            j=i-1 #The previous element
            k=i+1 #The next element
            while(0<=j and k<n):
                if(arr[j]+arr[k]==2*arr[i]): #a,a+1,a+2 This is an example of AP
                    table[i]=max(table[k]+1,table[i]) 
                    val=max(val,table[i])
                    j=j-1
                    k=k+1
                elif(arr[j]+arr[k]<2*arr[i]):
                        k=k+1
                else:
                        j=j-1
    print(val)
                    

           
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    arr=list(map(int,input().rstrip().rsplit()))
    solve(arr,n)
