"""
https://codeforces.com/problemset/problem/115/B
输入 n m(1≤n,m≤150) 和 n 行 m 列的网格图，每个格子要么是 G，要么是 W。

W 表示杂草。
你推着割草机，从左上角出发，目标是清除所有的杂草。
一开始你面朝右边。

你可以：
1. 如果你面朝右边，那么可以往右移动一步。
2. 如果你面朝左边，那么可以往左移动一步。
3. 往下移动一步，并改变朝向。
清除所有的杂草，最少需要移动多少步？
"""
'''
# 简单模拟（分类讨论）
n,m = map(int,input().split())

ans,cur = 0,0
h = 0
for i in range(n):
    s = input()
    l,r = None,None
    for j,x in enumerate(s):
        if x == 'W':
            if l is None:
                l = r = j
            else:
                r = j
    if l is None:
        continue
    h = i
    # 向左走
    if i % 2 == 0:
        if cur <= l:
            ans += r - cur
        else:
            ans += cur - l + r - l
        cur = r
    # 向右走
    else:
        if cur >= r:
            ans += cur - l
        else:
            ans += r - cur + r - l
        cur = l
print(ans + h)
'''



"""
==========================================================================
"""

'''
https://codeforces.com/problemset/problem/1969/C

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤3e5。
每组数据输入 n(1≤n≤3e5) k(0≤k≤10) 和长为 n 的数组 a(1≤a[i]≤1e9)。
如下操作，至多执行 k 次：
选择 a 中两个相邻元素 a[i] 和 a[i+1]，更新 a[i]=a[i+1]，或者更新 a[i+1]=a[i]。
输出 sum(a) 的最小值。
'''
# 区间dp,记忆化搜索
from functools import lru_cache
T = int(input())

for _ in range(T):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    # 表示对于前i个元素至多操作j次的最小和
    @lru_cache(None)
    def dfs(i,j):
        if i < 0:
            return 0
        ans = dfs(i - 1,j) + a[i]
        mi = a[i]
        for l in range(i - 1,max(i - j - 1,-1),-1):
            mi = min(mi,a[l])
            # (l,i)要操作t = i - l次
            t = i - l
            ans = min(ans,dfs(l - 1,j - t) + mi * (t + 1))
        return ans
    print(dfs(n - 1,k))
