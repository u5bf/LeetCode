#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode.cn/problems/combination-sum-ii/description/
#
# algorithms
# Medium (59.49%)
# Likes:    1527
# Dislikes: 0
# Total Accepted:    509.8K
# Total Submissions: 857K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用 一次 。
#
# 注意：解集不能包含重复的组合。 
#
#
#
# 示例 1:
#
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# 示例 2:
#
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
#
#
#
# 提示:
#
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#
#
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        state = []
        candidates.sort()
        n = len(candidates)
        def dfs(start, target):
            if 0 == target:
                res.append(list(state))
                return

            for i in range(start, n):
                if target - candidates[i] < 0:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                state.append(candidates[i])
                dfs(i+1, target - candidates[i])
                state.pop()

        dfs(0, target)
        return res
# @lc code=end

