
class SegmentTree:
    def __init__(self,arr,function):
        self.segment = [0 for x in range(3*len(arr)+3)]
        self.arr = arr
        self.fn = function
        self.make_tree(0,0,len(arr)-1)

    def make_tree(self,i,l,r):
        if l==r:
            self.segment[i] = self.arr[l]
        elif l<r:
            self.make_tree(2*i+1,l,int((l+r)/2))
            self.make_tree(2*i+2,int((l+r)/2)+1,r)
            self.segment[i] = self.fn(self.segment[2*i+1],self.segment[2*i+2])

    def __query(self,i,L,R,l,r):
        if l>R or r<L or L>R or l>r:
            return None
        if L>=l and R<=r:
            return self.segment[i]
        val1 = self.__query(2*i+1,L,int((L+R)/2),l,r)
        val2 = self.__query(2*i+2,int((L+R+2)/2),R,l,r)
      
        if val1 != None:
            if val2 != None:
                return self.fn(val1,val2)
            return val1
        return val2
        

    def query(self,L,R):
        return self.__query(0,0,len(self.arr)-1,L,R)


def newsum(i,j):
    maxm=0
    s=0
    for i in range(j):
        if arr[i]<0:
            maxm=max(maxm,s)
            s=0
        else:    
            s=s+arr[i]

    maxm=max(s,maxm)
    return maxm
n=int(input())
arr=list(map(int,input().split()))
seg=SegmentTree(arr,newsum)
m=int(input())
for i in range(m):
    l,r=map(int,input().split())
    l=l-1
    r=r-1
    print(seg.query(l,r))