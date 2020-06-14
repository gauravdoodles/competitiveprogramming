dx=[0,1,0,-1]
dy=[1,0,-1,0]
c=0
def dfs(x,y):
    global c
    c+=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if valid(xx,yy):
            dfs(xx,yy)

def valid(x,y):
    

    