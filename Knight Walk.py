def neighbour(s1,s2,n,m):    
    temp_arr=[]
    if s1+2<=n:
        if s2+1<=m:
            temp_arr.append([s1+2,s2+1])
        if s2-1>0:
            temp_arr.append([s1+2,s2-1])
    if s1-2>0:
        if s2+1<=m:
            temp_arr.append([s1-2,s2+1])
        if s2-1>0:
            temp_arr.append([s1-2,s2-1])
    if s2+2<=m:
        if s1+1<=n:
            temp_arr.append([s1+1,s2+2])
        if s1-1>0:
            temp_arr.append([s1-1,s2+2])
    if s2-2>0:
        if s1+1<=n:
            temp_arr.append([s1+1,s2-2])
        if s1-1>0:
            temp_arr.append([s1-1,s2-2])
    return (temp_arr)

def solve(n,m,a,b,c,d):
    
    dic={}
    if([a,b]==[c,d]):
        return 0
    else:
        dic[a,b]=1
    j=0
    val=1
    arr=neighbour(a,b,n,m)
    length=len(arr)
    while(arr):
        j=j+1
        visit=arr.pop(0)
        if(visit[0],visit[1]) not in dic.keys():
            dic[visit[0],visit[1]]=1
            if([visit[0],visit[1]] == [c,d]):
                return val
            else:
                temp=neighbour(visit[0],visit[1],n,m)
                arr=temp.copy()
        if(j==length):
            val=val+1
            length=length+len(arr)
    return(-1)
        

t=int(input())
while(t>0):
    t=t-1
    n,m=map(int,input().split())
    positions=list(map(int,input().rstrip().rsplit()))
    a=positions[0]
    b=positions[1]
    c=positions[2]
    d=positions[3]
    print(solve(n,m,a,b,c,d))















'''                if s2+1<=m:
			temp_arr.append([s1+2,s2+1])
		if s2-1>0:
			temp_arr.append([s1+2,s2-1])
	if s1-2>0:
		if s2+1<=m:
			temp_arr.append([s1-2,s2+1])
		if s2-1>0:
			temp_arr.append([s1-2,s2-1])
	if s2+2<=m:
		if s1+1<=n:
			temp_arr.append([s1+1,s2+2])
		if s1-1>0:
			temp_arr.append([s1-1,s2+2])
	if s2-2>0:
		if s1+1<=n:
			temp_arr.append([s1+1,s2-2])
		if s1-1>0:
			temp_arr.append([s1-1,s2-2])
	return (temp_arr)

def knight(n,m,s1,s2,d1,d2):
	arr=[]
	dic={}

	if [s1,s2]==[d1,d2]:
		return (0)
	else:
		dic[s1,s2]=1
	temp=look(s1,s2)
	for y in temp:
		arr.append(y)
	count= len(arr)
	j=0
	level=1
	while arr:
		j+=1
		ele= arr.pop(0)
		[t1,t2]=ele
# 		print (t1,t2)
		if (t1,t2) not in dic.keys():
			# print (level)
			dic[t1,t2]=1
			# print (dic)
			if [t1,t2]==[d1,d2]:
				return (level)
			else:
				temp=look(t1,t2)
				for y in temp:
					arr.append(y)
		if j==count:
			level+=1
			count= count+len(arr)
	return (-1)

if __name__=="__main__":
	t= int(input())
	for i in range(t):
		temp= list(map(int,input().split()))
		[n,m]=temp
		temp= list(map(int,input().split()))
		[s1,s2,d1,d2]=temp
		print (knight(n,m,s1,s2,d1,d2))

'''
