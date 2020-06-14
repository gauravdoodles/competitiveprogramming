
from sys import stdin
def solve(n):
    if n<12:
        return n
    if n in memo:
        return memo[n]
    memo[n]= solve(n//2)+solve(n//4)+solve(n//3)
    return memo[n]

while True:
    st=stdin.readline()
    memo={}

    if len(st.strip())==0:
        break
    ans=solve(int(st))
    print(ans)
