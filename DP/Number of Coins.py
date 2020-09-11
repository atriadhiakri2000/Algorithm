import math
MAX = 10000000000
def sol():
    cents,coins=map(int,input().split())
    coin_val=list(map(int,input().split()))
    
     dp = [MAX]*(cents+1)
    dp[0]=0
    
    for i in coin_val:
        for j in range(cents+1):
            if j>=i:
                dp[j]=min(dp[j],1+dp[j-i])
    
    if dp[cents]==MAX:
        print("-1")
    else:
        print(dp[cents])
    
t=int(input())
for i in range(t):
    sol()
