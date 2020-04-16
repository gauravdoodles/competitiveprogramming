n = int(input())

perm = [0] + list(map(int, input().split()))

 

index = 1

last = 1

dim = 0

 

ans = []

ans.append([])

visited = [True, True] + [False]*(n-1)

 

def first_unvisited():

    for i in range(n+1):

        if not visited[i]:

            return i

    else:

        return -1

 

 

while True:

    ans[dim].append(index)

    index = perm[index]

    visited[index] = True

 

    if index == last:

        unvisited_ind = first_unvisited()

        ans[dim].append(index)

        

        if unvisited_ind == -1:

            break

        else:

            index = unvisited_ind

            last = index

            ans.append([])

            dim+=1

 

print(dim+1)

for i in range(dim+1):

    print(" ".join(map(str, ans[i])))