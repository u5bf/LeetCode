#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    int cuttingBamboo(int bamboo_len) {
        if (bamboo_len <= 3) return bamboo_len - 1;

        int mod{1000000007};
        long long ans{1LL};
        long long x{3LL};
        // 快速幂
        for (int p = bamboo_len / 3 - 1; p != 0; p >>= 1) {
            if ((p & 1) == 1) ans = ans * x % mod;
            x = x * x % mod;
        }
        if (bamboo_len % 3 == 1) {
            return ans  * 4 % mod;
        } else if (bamboo_len % 3 == 2) {
            return 6 * ans % mod;
        }
        return ans * 3 % mod;
    }
};

int main(int argc, char const *argv[])
{
    std::cin.tie(nullptr)->std::ios::sync_with_stdio(false);
    cout << Solution().cuttingBamboo(127) << endl;
    return 0;
}

