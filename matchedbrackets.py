n=int(input())
s=list(map(int,input().split()))
maxdepth=0
maxsymbol=0
depth=0
for i in range(n):
	if depth==0:
		numsymbol=0
		maxmatch=i+1

	if s[i]==1:
		depth+=1
		if depth>maxdepth:
			maxdepth=depth
			depthindex=i+1
	else:
		depth=depth-1
	if depth==0 and numsymbol>maxsymbol:
		maxsymbol=numsymbol+1
		symbolindex=maxmatch
	if depth!=0:
		numsymbol+=1
print(maxdepth,depthindex,maxsymbol,symbolindex)