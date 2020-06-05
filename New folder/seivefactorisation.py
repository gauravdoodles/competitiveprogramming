maxn=1000001


def seivefact():
    arr=[-1 for i in range(maxn+1)]
    for i in range(2,maxn+1):
        if arr[i]==-1:
            j=i
            while(j<=maxn):
                if arr[j]==-1:
                    arr[j]=i
                j=j+i
    return arr



print(seivefact())
