def process2(M,A,n):
	i,j=0,0
	for i in range(n):
		M[i][0]=i
	j=1
	while(1<<j<=n):
		while(i+(1<<j)-1<n):
			if (A[M[i][j-1]]<A[M[i+(1<<(j-1))][j-1]]):
				M[i][j]=M[i][j-1]
			else:
				M[i][j]=M[i+(1<<(j-1))][j-1]
			i+=1
		j+=1


