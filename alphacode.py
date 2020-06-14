
def issafe(pos):
    global n
    if pos+1<n:
        return True
    return False

def solve(pos,st):
    global n
    if pos>n-1:
        return 0
    z=0
    if issafe(pos):
        z=st[pos]*10+st[pos+1]
    x=0
    if st[pos]<=26:
        x=1+solve(pos+1, st)
    y=0
    if z>=10 and z<=26 :
        y=1+solve(pos+2, st)
    return x+y
while(True):
    nt=input()
    n=len(nt)

    if nt=='0':
        break
    st=[]
    for i in nt:
        st.append(int(i))

    ans=solve(0, st)
    print(ans)
