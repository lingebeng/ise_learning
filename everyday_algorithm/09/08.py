
"""周赛414，第2题（3281）
给你一个整数数组 start 和一个整数 d，代表 n 个区间 [start[i], start[i] + d]。

你需要选择 n 个整数，其中第 i 个整数必须属于第 i 个区间。所选整数的 得分 定义为所选整数两两之间的 最小 绝对差。

返回所选整数的 最大可能得分 。



示例 1：

输入： start = [6,0,3], d = 2

输出： 4

解释：

可以选择整数 8, 0 和 4 获得最大可能得分，得分为 min(|8 - 0|, |8 - 4|, |0 - 4|)，等于 4。
"""

# 就是一个二分寻找右边界，不过wa了一发，没有把控好右边界，还是要好好分析题意的！

"""
wa 1
[1000000000,0]
1000000000
"""

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        interval = [[x,x + d] for x in start]
        interval.sort()


        def check(x):
            start = interval[0][0]
            for l,r in interval[1:]:
                if start + x <= r:
                    if start + x < l:
                        start = l
                    else:
                        start += x
                else:
                    return False
            return True

        left,right = 0,2 * 10 ** 9

        while left < right:
            mid = left + right + 1 >> 1
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left


"""周赛414，第3题（3282）
给你一个长度为 n 的整数数组 nums 。
你的目标是从下标 0 出发，到达下标 n - 1 处。每次你只能移动到 更大 的下标处。
从下标 i 跳到下标 j 的得分为 (j - i) * nums[i] 。
请你返回你到达最后一个下标处能得到的 最大总得分 。
 
示例 1：

输入：nums = [1,3,1,5]

输出：7
解释：

一开始跳到下标 1 处，然后跳到最后一个下标处。总得分为 1 * 1 + 2 * 3 = 7 。
"""

# 这题就是一个贪心，比赛时想了一个O(n^2)的dp，就跟最长上升子序列一样，一直在想怎么优化，比如线段树优化，二分优化
# 没想到竟然是个思维贪心，还是自己思维跟不上，长时间没训练了，今后得重新抓起来了！

# 没想到竟然是贪心，也怪自己太笨！
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        # 跳的话，每次都必须跳到更大的数那里，否则不如不跳！
        # 确实如此！
        n = len(nums)
        lst = [(-1,-1)]
        for i,x in enumerate(nums):
            if x > lst[-1][-1]:
                lst.append((i,x))
        lst.append((n - 1,None))
        ans = 0
        for (i,x),(j,_) in pairwise(lst[1:]):
            ans += x * (j - i)
        return ans