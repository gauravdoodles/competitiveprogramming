
memo={}

def getans(n,f,h,k1,k2,z1,z2):

    if n==0:
        return 1

    if (n,f,h,k1,k2,z1,z2) in memo:
        return memo[(n,f,h,k1,k2,z1,z2)]
    x=0
    if f>0 and k1>0:
        x=getans(n-1,f-1,h,k1-1,z2,z1,z2)
    y=0
    if h>0 and k2>0:
        y=getans(n-1,f,h-1,z1,k2-1,z1,z2)
    memo[(n,f,h,k1,k2,z1,z2)]=x+y
    return x+y

n1,n2,k1,k2=map(int,input().split())
print(getans(n1+n2,n1,n2,k1,k2,k1,k2))