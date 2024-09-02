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