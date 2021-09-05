import itertools as it
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0])

        s = list(it.product(range(2), repeat = N))

        for i in s:
            res = [str(j) for j in i]
            res = "".join(list(res))
            if res not in nums:
                return res
