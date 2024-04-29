#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode.cn/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (66.79%)
# Likes:    1056
# Dislikes: 0
# Total Accepted:    405.9K
# Total Submissions: 606.7K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
#
#
# 示例 1:
#
#
#
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
#
#
# 示例 2:
#
#
# 输入: [1,null,3]
# 输出: [1,3]
#
#
# 示例 3:
#
#
# 输入: []
# 输出: []
#
#
#
#
# 提示:
#
#
# 二叉树的节点个数的范围是 [0,100]
# -100  
#
#
#
from collections import deque
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(node.val)
        return ans
# @lc code=end

