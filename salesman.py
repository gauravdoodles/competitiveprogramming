def build(idx,low,high):
	if low==high:
		tree[idx]=arr[low][0]
		return

	mid=(low+high)>>1
	build(idx<<1,low,mid)
	build(idx<<1|1,mid+1,high)
	tree[idx]=max(tree[idx<<1],tree[idx<<1|1])

def push(idx,low,high):
	if lazy[idx]:
		tree[idx]+=lazy[idx]
		if low!=high:
			lazy[idx<<1]+=lazy[idx]
			lazy[idx<<1|1]+=lazy[idx]
		lazy[idx]=0

def add(idx,low,high,l,r,val):
	push(idx,low,high)
	if low>r or high<l:
		return
	if low>=l and high<=r:
		lazy[i]+=val
		push(idx,low,high)
		return 
	mid=(low+high)>>2
	add(idx<<1,low,mid,l,r,val)
	add(idx<<1|1,mid+1,high,l,r,val)
	tree[idx]=max(tree[idx<<1],tree[idx<<1|1])

def getelement(idx,low,high,pos):
	push(idx,low,high)
	if low==high:
		return low
	mid=(low+high)>>1
	push(idx<<1,low,mid)
	push(idx<<1|1,mid+1,high)
	if pos<=middle:
		return getelement(idx<<1,low,mid,val)

	else:
		return lowerbound(idx<<1|1,mid+1,high,value)
def lowerbound(idx,low,high,val):
	push(idx,low,high)
	if tree[idx]<val:
		return high+1
	if low==high:
		return low

	mid=(low+high)>>1
	push(idx<<1,low,mid)
	push(idx<<1|1,mid+1,high)
	if tree[idx<<1]>=val:
		return lowerbound(idx<<1,low,high,val)
	else:
		return lowerbound(idx<<1|1,mid+1,high,val)

def upperbound(idx,low,high,val):
	return lowerbound(idx,low,high,val+1)

if __name__ == '__main__':
	n,q=map(int,input().split())
	
	for i in range(n):
		arr=list(map(int,input().split()))
	data=[]
	for i in range(len(arr)):
		data.append([arr[i],i])
	pos=[0 for i in range(n)]
	data.sort()
	whois=[0 for i in range(n)]
	for i in range(n):
		a,b=arr[i]
		pos[b]=i
		whois[i]=arr[b]

	tre=[0 for k in range(n<<2|1)]
	build(0,0,n-1)
	for _ in range(q):
		type1,x=map(int,input().split())
		if type1==1:
			previous=x
			previouspos=pos[x]
			previousvalue=getelement(0,0,previouspos)
			currentpos=upperbound(0,0,previousvalue)-1
			currentid=whois[currentpos]
			if previous==currentid:
				add(0,0,n-1,previouspos,previouspos,1)
			else:
				pos[previous],pos[currentid]=pos[currentid],pos[previous]
				whois[previous],whois[currentid]=whois[currentid],whois[previous]
				add(0,0,n-1,currentpos,currentpos,1)

		elif type1==2:
			print(n-lowerboud(0,0,n-1,c)+1)
		else:
			lb=lowerbound(0,0,n-1,x)
			if lb!=n:
				add(0,0,n-1,lb,n-1,-1)







