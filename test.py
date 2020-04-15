def binary_search(arr,key,l):
    low=l
    high=len(arr)-1
    while(low<=high):
        mid=(high+low)//2
        if arr[mid][0]<=key:
            low=mid+1
        else:
            high=mid-1

    return low


def prefix_sum(arr):
    prefix=[0 for i in range(len(arr))]
    prefix[0]=arr[0][2]
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i][2]
    return prefix

for _ in range(int(input())):
    n=int(input())
    arr=[]
    for t in range(n):
        arr.append(list(map(int,input().split())))
    arr=sorted(arr,key=lambda x:x[0])
    prefix=prefix_sum(arr)
    max_result=0
    for i in range(n-1):
        result=arr[i][2]
        low=i+1
        idx=binary_search(arr,arr[i][1],low)
        result=result+prefix[n-1]-prefix[idx-1]
        max_result=max(max_result,result)

    print(max_result)


