def solve(n,i,k):
    if n<arr[i][0] or i<k:
        return 0

    ans=0

    ans+=arr[i][1]

    solve(n, i+1)

    return ans