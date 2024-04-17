#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    int iceBreakingGame(int num, int target) {
        // if (num == 1) return 0;
        // return (iceBreakingGame(num - 1, target) + target) % num;
        int ans{};
        for (int i = 2; i <= num; ++i) {
            ans = (target + ans) % i;
        }
        return ans;
    }
};

int main(int argc, char const *argv[])
{
    std::cin.tie(nullptr)->std::ios::sync_with_stdio(false);
    // cout << Solution() << endl;
    return 0;
}

