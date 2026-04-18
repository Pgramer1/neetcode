class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i,n in enumerate(nums):
            if i ^ n != 0:
                return n-1
        return n + 1       