r,c,d=map(int,input().split())
arr=[]
for i in range(r):
	temp=list(map(int,input().split()))
	arr.append(temp)
def isvalid(x,y):
	return x<r and y<c and arr[x][y]!=0


memo={}

def solve(i,j,step,direction,d):
	if not isvalid(i,j):
		return 0

	if i==r-1 and j==c-1:
		return 1

	if (i,j,step,direction,d) in memo:
		return memo[(i,j,step,direction,d)]
	ans=0
	if direction==1:
		if step<d:
			ans=(ans+solve(i,j+1,step+1,1,d))%2011

		ans=(ans+solve(i+1,j,1,2,d))%2011
	else:
		if step<d:
			ans=(ans+solve(i+1,j,step+1,2,d))%2011

		ans=(ans+solve(i,j+1,1,1,d))%2011
	memo[(i,j,step,direction,d)]=ans
	return ans

if len(arr)<1:
	print(0)
else:
	zzz=solve(0,0,0,1,d)
	print(zzz)

