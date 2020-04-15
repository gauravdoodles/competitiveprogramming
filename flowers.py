#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10
class SegmentTree:
    def __init__(self, arr, function):
        self.tree = [None for _ in range(len(arr))] + arr
        self.size = len(arr)
        self.fn = function
        self.build_tree()

    def build_tree(self):
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.fn(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, p, v):
        p += self.size
        self.tree[p] = v
        while p > 1:
            p = p // 2
            self.tree[p] = self.fn(self.tree[p * 2], self.tree[p * 2 + 1])

    def query(self, l, r):
        l, r = l + self.size, r + self.size
        res = None
        while l <= r:
            if l % 2 == 1:
                res = self.tree[l] if res is None else self.fn(res, self.tree[l])
            if r % 2 == 0:
                res = self.tree[r] if res is None else self.fn(res, self.tree[r])
            l, r = (l + 1) // 2, (r - 1) // 2
        return res

n=int(input())
h=list(map(int,input().split()))
b=list(map(int,input().split()))
new_arr=[]
for i in range(n):
    new_arr.append([h[i],b[i],i])
new_arr.sort(key=lambda x: x[0])
new_arr=new_arr[::-1]

ans=[0 for i in range(n)]
seg=SegmentTree(ans,max)

for seq in new_arr:
    idx=seq[2]
    new_value=seg.query(idx,n-1)
    new_value+=seq[1]
    #ans[idx]=new_value
    seg.update(idx,new_value)
mx=seg.query(0,n-1)
print(mx)

