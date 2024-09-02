# https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/description/?envType=daily-question&envId=2024-09-02
# 统计最大连续的T与F，取一个max即可！
from collections import Counter

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        cnt1,cnt2 = Counter(),Counter()
        ans1,ans2 = 0,0
        left1,left2 = 0,0
        for right,x in enumerate(answerKey):
            cnt1[x] += 1
            cnt2[x] += 1
            while cnt1['T'] > k:
                ans1 = max(ans1,right - left1)
                cnt1[answerKey[left1]] -= 1
                left1 += 1
            ans1 = max(ans1,right - left1 + 1)
            while cnt2['F'] > k:
                ans2 = max(ans2,right - left2)
                cnt2[answerKey[left2]] -= 1
                left2 += 1
            ans2 = max(ans2,right - left2 + 1)
        return max(ans1,ans2)


# https://codeforces.com/problemset/problem/437/C
# 删除一个无向图的所有节点，删除一个节点的代价是该节点所有相邻未删除的节点点权之和，求删除所有节点的最小代价
# 贪心思考，按边删除，去取最小值加入答案！

n,m = map(int,input().split())
a = list(map(int,input().split()))

ans = 0

for _ in range(m):
    u,v = map(int,input().split())
    ans += min(a[u - 1],a[v - 1])

print(ans)
