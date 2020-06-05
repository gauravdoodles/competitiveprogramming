def combine(left,right):
    z=min(left[1],right[2])
    a=left[0]+right[0]+z
    b=left[1]+right[1]-z
    c=left[2]+right[2]-z
    return (a,b,c)


def build(idx,l,r):
    if l==r:
        if string[l]=='(':
            tree[1]+=1
        else:
            tree[2]+=1
    else:
        mid=(l+r)//2
        build(2*idx+1,l,mid)
        build(2*idx+2,mid+1,r)
        tree[idx]=combine(tree[2*idx+1],tree[2*idx+2])

def query(idx,x,y,l,r):
    if l>=y or x>=r:
        return (0,0,0)
    if x<=l and r<=y:
        return tree[idx]
    mid=(l+r)//2
    left=query(2*idx+1,x,y,l,mid)
    right=query(2*idx+2,x,y,mid+1,r)
    
    return combine(left,right)


if __name__ == '__main__':
    string=input()
    n=len(string)
    m=int(input())
    tree=[(0,0,0) for i in range(5*n)]
    build(0,0,n-1)
    for i in range(m):
        a,b=map(int,input().split())
        a=a-1
        b=b-1
        ans=query(0,a,b,0,n-1)
        print(ans)
    