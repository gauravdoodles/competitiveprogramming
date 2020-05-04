
from sys import stdin,stdout
def build_tree(idx,l,r):
	if l==r:
		tree[idx].append(arr[l])
	else:
		mid=(l+r)//2
		build_tree(2*idx+1,l,mid)
		build_tree(2*idx+2,mid+1,r)
		tree[idx]=merge(tree[2*idx+1],tree[2*idx+2])


def merge(left,right):
	myList=[]
	i=0
	j=0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:

			myList.append(left[i])

			i += 1
		else:
			myList.append(right[j])
			j += 1



	while i < len(left):
		myList.append(left[i])
		i += 1


	while j < len(right):
		myList.append(right[j])
		j += 1
		
	return myList


def countGreater(arr, n, k): 
	l = 0
	r = n - 1
	leftGreater = n 

	while (l <= r): 
		m = int(l + (r - l) / 2) 

		if (arr[m] > k): 
			leftGreater = m 
			r = m - 1
		else: 
			l = m + 1
	return (n - leftGreater) 

def query(idx,l,r,x,y,key):
	if x>r or y<l:
		return 0

	if x<=l and r<=y:
		return  countGreater(tree[idx],len(tree[idx]),key)
	mid=(l+r)//2
	return query(2*idx+1,l,mid,x,y,key)+query(2*idx+2,mid+1,r,x,y,key)








if __name__ == '__main__':
	n=int(stdin.readline())
	sys.setrecursionlimit(5*n)
	arr=list(map(int,stdin.readline().split()))
	q=int(stdin.readline())
	tree=[[] for i in range(4*n-1)]
	build_tree(0,0,n-1)
	print(tree)

	for i in range(q):
		x,y,key=map(int,stdin.readline().split())
		x=x-1
		y=y-1
	
		ans=query(0,0,n-1,x,y,key)
		stdout.write(str(ans))




