#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    int cuttingBamboo(int bamboo_len) {
        if (bamboo_len <= 3) return bamboo_len - 1;
        int ans = pow(3, bamboo_len / 3);
        if (bamboo_len % 3 == 1) {
            ans = ans / 3 * 4;
        } else if (bamboo_len % 3 == 2) {
            ans *= 2;
        }
        return ans;
    }
};

int main(int argc, char const *argv[])
{
    std::cin.tie(nullptr)->std::ios::sync_with_stdio(false);
    Solution();
    return 0;
}

