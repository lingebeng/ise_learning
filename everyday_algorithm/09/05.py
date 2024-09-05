"""
https://codeforces.com/problemset/problem/213/B
输入 n(1≤n≤100) 和长为 10 的数组 a(0≤a[i]≤100)。
有多少个长度为至多为 n 的正整数，无前导零，且数字 0~9 分别至少出现 a[0],a[1],...,a[9] 次？
答案模 1e9+7。
"""
# 数形 dp
MOD = 10 ** 9 + 7
C = [[0] * 101 for _ in range(101)]

for i in range(101):
    C[i][0] = 1
    for j in range(1,101):
        C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

n  = int(input())
cnt = list(map(int, input().split()))
# 表示 还有 i 个位置是空的，还剩下[j,9]数字没填
from functools import lru_cache
@lru_cache(None)
def dfs(i,j):
    if j == 9:
        if i < cnt[9]:
            return 0
        return 1
    # 不能有前导0，当 j = 0时，有 C[i - 1][k_cnt_num]种选择！
    w = i - (j == 0)
    res = 0
    for k in range(cnt[j],i + 1):
        res = (res + dfs(i - k,j + 1) * C[w][k]) % MOD
    return res
ans = 0
for i in range(1,n + 1):
    ans += dfs(i,0)

ans %= MOD

print(ans)










