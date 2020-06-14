def cal(i,j,a,b,k):
    if i==len(a):
        return (len(b)-j)*k 

    if j==len(b):
        return (len(a)-i)*k
    if (i,j) in memo:
        return memo[(i,j)]



    memo[(i,j)]= min(cal(i+1,j+1,a,b,k)+abs(ord(a[i])-ord(b[j])),cal(i+1, j, a, b, k)+k,cal(i, j+1, a, b, k)+k)
    return memo[(i,j)]



a=input()
b=input()
k=int(input())
n1=len(a)
n2=len(b)

#dp=[[-1 for i in range(n1+100)] for j in range(n2+100)]
memo={}
ans=cal(0, 0, a, b, k)
print(ans)

