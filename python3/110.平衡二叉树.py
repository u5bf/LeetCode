#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode.cn/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (58.24%)
# Likes:    1496
# Dislikes: 0
# Total Accepted:    593.4K
# Total Submissions: 1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是 平衡二叉树  
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#
#
# 示例 3：
#
#
# 输入：root = []
# 输出：true
#
#
#
#
# 提示：
#
#
# 树中的节点数在范围 [0, 5000] 内
# -10^4 <= Node.val <= 10^4
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) != -1
# @lc code=end

