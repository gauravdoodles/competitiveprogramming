'''
given an array=[2,4,6,9,10] and two integers L,R you have to find gcd of all numbers from L to R excluding L,R'''

from math import gcd

array=[2,4,6,9,10]
def pre(arr,n):
    pre=[0 for i in range(n)]
    pre[0]=arr[0]
    for i in range(1,n):
        pre[i]=gcd(arr[i],pre[i-1])


    return pre

def suf(arr,n):
    suf=[0 for i in range(n)]
    suf[n-1]=arr[n-1]
    for i in range(n-2,0):
        suf[i]=gcd(arr[i],suf[i+1])

    return suf


n=len(array)
pre=pre(array, n)
suf=suf(array, n)
print(gcd(pre[1],suf[3]))