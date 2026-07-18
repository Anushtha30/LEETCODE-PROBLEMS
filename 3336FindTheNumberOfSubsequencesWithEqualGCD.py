from math import gcd
from functools import cache

class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7

        @cache
        def dfs(i, g1, g2):
            if i == len(nums):
                return 1 if g1 == g2 and g1 != 0 else 0

            x = nums[i]

            ans = dfs(i + 1, g1, g2)

            ans += dfs(i + 1,
                       gcd(g1, x) if g1 else x,
                       g2)

            ans += dfs(i + 1,
                       g1,
                       gcd(g2, x) if g2 else x)

            return ans % MOD

        return dfs(0, 0, 0)