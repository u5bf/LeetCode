/*
 * @lc app=leetcode.cn id=42 lang=cpp
 *
 * [42] 接雨水
 *
 * https://leetcode.cn/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (63.33%)
 * Likes:    5103
 * Dislikes: 0
 * Total Accepted:    921.6K
 * Total Submissions: 1.5M
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * 输出：6
 * 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
 *
 *
 * 示例 2：
 *
 *
 * 输入：height = [4,2,0,3,2,5]
 * 输出：9
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == height.length
 * 1 <= n <= 2 * 10^4
 * 0 <= height[i] <= 10^5
 *
 *
 */

// @lc code=start
class Solution {
public:
    int trap(vector<int>& height) {
        stack<int> stk;
        int ans{};
        int n = height.size();
        for (int i{}; i < n; ++i) {
            while (!stk.empty() && height[i] >= height[stk.top()]) {
                int bottom_h = height[stk.top()];
                stk.pop();
                if (stk.empty()) break;// 只有底没有左边的高度，接不了雨水
                int w = i - stk.top() - 1;
                int h = min(height[i], height[stk.top()]) - bottom_h;
                ans += w * h;
            }
            stk.push(i);
        }
        return ans;
    }
};
// @lc code=end

