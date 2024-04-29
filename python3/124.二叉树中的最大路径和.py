#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (45.49%)
# Likes:    2208
# Dislikes: 0
# Total Accepted:    404.4K
# Total Submissions: 889.1K
# Testcase Example:  '[1,2,3]'
#
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个
# 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
#
# 示例 2：
#
#
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#
#
#
#
# 提示：
#
#
# 树中节点数目范围是 [1, 3 * 10^4]
# -1000 <= Node.val <= 1000
#
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float("inf")

        def dfs(node):
            if not node:
                return 0
            lsum = dfs(node.left)
            rsum = dfs(node.right)
            cur = node.val
            if lsum > 0:
                cur += lsum

            if rsum > 0:
                cur += rsum

            nonlocal ans
            ans = max(ans, cur)

            if (lrmax := max(lsum, rsum)) > 0:
                return node.val + lrmax

            return node.val

        dfs(root)
        return ans


# @lc code=end
