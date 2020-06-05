n,q=map(int,input().split())
blk=555
for i in range(q):
    l=query[0]
    r=query[1]

    while(ml>l):
        ml-=1
        add(ml)

    while(mr<r):
        mr+=1
        add(mr)

    while ml<l:
        remove(ml)
        ml+=1
    while mr>r:
        remove(mr)
        mr-=1

cnt=0
def add(pos):
    global cnt
    freq[arr[pos]]+=1
    if freq[arr[pos]]==1:
        cnt+=1


def remove(pos):
    global cnt
    freq[arr[pos]]-=1
    if freq[arr[pos]]==0:
        cnt-=1

def cmp(a,b):
    if a[0]//blk!=b[0]//blk:
        return a[0]//blk<b[0]//blk
    return a[1]<b[1]



