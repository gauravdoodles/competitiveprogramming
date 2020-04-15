'''
n=int(input())
arr=[]
for _ in range(n):
	l1=list(map(int,input().split()))
	arr.append(l1)
dp=[0 for i in range(1<<n)]
dp[0]=1
for men in range((1<<n)-1):
	setbits=bin(men).count('1')
	for women in range(n):
		if (arr[setbits][women] and (men&(1<<women))==0):
			m2=men^(1<<women)
			dp[m2]+=dp[men]
'''
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]



M = 10 ** 9 + 7
cur = [0] * (1 << N)
cur[0] = 1

for B in A:
	nxt = [0] * (1 << N)
	C = [1 << i for i, v in enumerate(B) if v == 1]
	print(c)
	for s, v in enumerate(cur):
		if v == 0:
			continue
		v %= M
		for b in C:
			if (s & b) != 0:
				continue
			nxt[s | b] += v
	cur = nxt
print(cur[(1 << N) - 1] % M)

print(dp[(1<<n)-1])