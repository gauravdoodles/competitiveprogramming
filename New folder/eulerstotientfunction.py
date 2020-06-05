


def phi1(n):
    ''' 
    sqrt(n)
    '''
    res=n
    i=2
    while(i*i<=n):
        if n%i==0:
            res=res//i
            res=res*(i-1)

            while(n%i==0):
                n=n//i

        i+=1

    if n>1:
        res=res//n
        res=res*(n-1)
    return res


'''
log(log(n))
'''
def phi2(maxn):
    phi=[]
    for i in range(maxn+2):
        phi.append(i)

    for i in range(2,maxn+2):
        if phi[i]==i:
            for j in range(i,maxn+2,i):
                phi[j]=phi[j]//i
                phi[j]*=(i-1)


    return phi[maxn]



t=10
while(t):
    n=int(input())

    print(phi1(n))
    print(phi2(n))

