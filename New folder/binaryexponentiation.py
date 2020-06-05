def biex(a,n):
    res=1
    while(n):
        if n%2:
            res=res*a
            n=n-1
        else:
            a=a*a
            n=n//2
    return res

def modex(a,n,p):
    res=1
    while(n):
        if n%2:
            res=(res*a)%p
            n=n-1

        else:
            a=(a*a)%p
            n=n//2

    return res
print(biex(2,6))
print(modex(2,6,2))