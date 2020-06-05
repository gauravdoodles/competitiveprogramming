def upd(idx,l,r,x):
    lazy[idx]+=x
    s[idx]+=(r-l)*x

def shift(id,l,r):
    mid=(l+r)//2
    upd(2*idx+1,l,mid,lazy[idx])
    upd(2*idx+2,mid+1,r,lazy[idx])
    lazy[idx]=0


def increase(x,y,val,idx,l,r):
    if x>=r or l>=y:
        return 0
    if x<=l and r<=y:
        upd(idx,l,r,val)
    shift(idx,l,r)
    mid=(l+r)//2
    increase(x,y,val,2*idx+1,l,mid)
    increase(x,y,val,2*idx+2,mid+1,r)
    s[idx]=s[2*idx+1]+s[2*idx+2]

def calsum(x,y,idx,l,r):
    if x>=r or l>=y:
        return 0
    if x<=l and r<=y:
        return s[idx]
    shift(idx,l,r)
    return calsum(x,y,2*idx+1,l,mid)+calsum(x,y,idx,2*idx+2,mid+1,r)




if __name__ == '__main__':
    arr=[1,2,3,4,5]
    n=5
    s=[0 for i in range(2*n)]
    lazy=[0 for j in range(2*n)]
    ans1=calsum(0, n-1, idx=0, l=0, r=n-1)
    increase(0, n-1, 1, idx=0, l=0, r=n-1)