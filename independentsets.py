# n=int(input())
# graph=[[]for i in range(n)]
# for _ in range(n-1):
# 	u,v=map(int,input().split())
# 	graph[u-1].append(v-1)
# 	graph[v-1].append(u-1)

# colour=[0 for i in range(n)]
# print(graph)
# def dfs(parent):
# 	ans=0
# 	if colour[parent]==0:
# 		return 
# 	count_black=0
# 	for child in graph[parent]:
# 		if colour[child]:
# 			count_black+=1
# 	if not count_black:
# 		colour[parent]=1
# 		ans+=1
# 	for child in graph[parent]:
# 		1 + dfs(child)
# 	return ans
# print(dfs(0))


#k=list(map(int,list(input())))
k=[1,2,3]
print(k)
