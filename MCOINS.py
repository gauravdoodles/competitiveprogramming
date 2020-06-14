def solve(n,k,l):
    if n<=0:
        return 0
    if n==k:
        return 1
    if n==l:
        return 1
    if n==1:
        return 1
    if n in memo:
        return memo[n]
    x=solve(n-k, k, l)
    y=solve(n-l, k, l)
    z=solve(n-1, k, l)
    memo[n]=not(x&y&z)

    return memo[n]
#to be solved still not correct
memo={}
ans=solve(25714, 2, 3)
print(ans)