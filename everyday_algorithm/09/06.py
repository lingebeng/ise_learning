""" 1
输入 A、B,输出有都多少个x，重排A、B、x，使其满足 p、q、r： q - p = r - q

r + p = 2q
"""
# 列举一下情况就行，用set去重！
A,B = map(int,input().split())

s = set()

if (A + B) % 2 == 0:
    s.add((A + B) // 2)

s.add(2 * A - B)
s.add(2 * B - A)

print(len(s))


"""2
有n次操作
每次操作用 左手或右手按钢琴键 Ai，移动手指到别的钢琴键需要消耗 |Ai - Aj|能量
求弹奏完整个钢琴，消耗的最少能量！
3
2 L
2 L
100 L
"""
# 直接模拟就行，我还以为是啥高级算法呢，结果就是开始时左右手放在对应开始的按键就行
n = int(input())
l,r = [],[]

for _ in range(n):
    a,b = input().split()
    if b == 'L':
        l.append(int(a))
    else:
        r.append(int(a))
ans = 0
for i in range(len(l) - 1):
    ans += abs(l[i] - l[i + 1])
for i in range(len(r) - 1):
    ans += abs(r[i] - r[i + 1])

print(ans)


"""3
给定一个长度为n的整数数组a，
找出数对(l,r)的数量，满足 a[l,r]为等差数列
"""
# 做一个差分数组找规律即可
# 注意 n = 1的情况特判，不然就RE了，因为d数组下标越界，不存在了！
n = int(input())
a = [*map(int,input().split())]
if n == 1:
    print(1)
    exit()

d = [a[i + 1] - a[i] for i in range(n - 1)]

ans = n
pre = d[0]
cnt = 0
for x in d:
    if x == pre:
        cnt += 1
    else:
        ans += cnt * (cnt + 1) // 2
        cnt = 1
        pre = x

ans += cnt * (cnt + 1) // 2

print(ans)


"""4
有n个能量为Ai的怪兽，每次可以选择打或不打，
如果打，就会获得Ai的经验，否则没有！
于此同时，加了一个加成，如果该怪兽是第偶数次被打败的，那么将会获得双倍经验！
也因此，如果打败所有怪兽，获得的经验不一定是最大的！
"""
# 一个简单的动态规划，用Kimi做了翻译，结果把思路给弄出来了，我还没想，也不知道自己独立思考能不能想到DP，感觉挺简单的，应该可以想出来！
# dp[i][0]表示，前i个怪兽中，已经打了偶数个怪兽获得的经验
# dp[i][1]表示，前i个怪兽中，已经打了奇数个怪兽获得的经验

n = int(input())
a = [*map(int, input().split())]

dp = [[0,0] for _ in range(n)]

dp[0] = [0,a[0]]

for i in range(1,n):
    dp[i][0] = max(dp[i - 1][1] + a[i] * 2,dp[i - 1][0])
    dp[i][1] = max(dp[i - 1][0] + a[i],dp[i - 1][1])

print(max(dp[-1]))

"""
嘿嘿，kimi给的题意，直接复制了
这段话描述了一个关于岛屿和桥梁的旅行问题。具体内容如下：

有 N 个岛屿和 M 座双向桥梁，岛屿和桥梁分别编号为 1, 2, ...,N  和 1, 2, ..., M。
桥梁 i 连接岛屿 Ui 和 Vi，并且无论哪个方向穿越这座桥梁都需要时间 Ti。
没有桥梁连接岛屿自身，但两个岛屿之间可能由多座桥梁直接连接。
可以使用一些桥梁在任何两个岛屿之间旅行。
接下来，问题描述了 Q 个查询，每个查询如下：

给定 Ki 座不同的桥梁：桥梁 Bi1,Bi2,BiK。
需要找到从岛屿 1 到岛屿 N 旅行的最小时间，同时至少使用一次这些桥梁。
只考虑过桥的时间，不考虑其他因素。
可以按照任何顺序和任何方向穿越给定的桥梁。
这个问题是一个典型的图论问题，涉及到寻找一个包含特定边的最短路径
"""
# 2024-09-06 17：54 好吧，此时我没有思路，等一会看一波题解！

from math import inf
from itertools import permutations

n,m = map(int,input().split())

Bridges = [(0,0,0) for _ in range(m + 1)]
g = [[inf] * (n + 1) for _ in range(n + 1)]

for i in range(1,m + 1):
    u,v,w = map(int,input().split())
    g[u][v] = min(g[u][v], w)
    g[v][u] = min(g[v][u], w)
    Bridges[i] = (u,v,w)

for i in range(n + 1):
    g[i][i] = 0

# floyd 求任意两点的最短路！ O(n ^ 3)
for k in range(1,n + 1):
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            g[i][j] = min(g[i][j],g[i][k] + g[k][j])

q = int(input())

for _ in range(q):
    ans = inf
    k = int(input())
    bridge_ids = list(map(int,input().split()))

    for bridge in permutations(bridge_ids):
        # 若某位为1,则代表端点相反，正好可以枚举所有端点状态！
        for i in range(1 << k):
            pre = 1
            tmp = 0
            for j in range(k):
                u,v,w = Bridges[bridge[j]]
                if (i >> j) & 1:
                    u,v = v,u
                tmp += g[pre][u]
                tmp += w
                pre = v
            tmp += g[pre][n]
            ans = min(ans, tmp)
    print(ans)

# 2024-09-06 21：05 好吧，没想到答案是暴力枚举，但是枚举的很有技巧，将二进制与集合的关系用得很好！

# 思路就是通过flod求出任意两点之间的距离，然后枚举所有可能的路线，前提是包含指定桥的编号！