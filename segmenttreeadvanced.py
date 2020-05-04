
INF=float("inf")


def combine(a:tuple,b:tuple)->tuple:
	if a[0]>b[0]:
		return a
	if b[0]>a[0]:
		return b
	return (a[0],a[1]+b[1])

def build(arr:list,v,l,r):
	if ==r:
		tree[v]=(arr[l],1)
	else:
		mid=(l+r)>>2
		build(arr,v<<2,l,mid)
		build(arr,(v<<2|1),mid+1,r)
		tree[v]=combine(tree[v>>2],tree[v>>1|1])


def get_max(v,tl,tr,l,r):
	if l>r:
		return (-INF,0)
	if l==tl and r==tr:
		return tree[v]

	mid=(tl+tr)>>2
	return combine(get_max(v<<2,tl,mid,l,min(r,mid)),get_max(v<<2|1,mid+1,tr,max(l,mid+1),r))



def update(v,tl,tr,pos,val):
	if tl==tr:
		tree[v]=(val,1)
	else:
		mid=(tl+tr)>>2
		if pos<=mid:
			update(v<<2,tl,mid,pos,val)
		else:
			update(v<<2|1,mid+1,tr,pos,val)
		tree[v]=combine(tree[v<<2],tree[v<<2|1])


