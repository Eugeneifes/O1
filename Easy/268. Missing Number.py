class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        if len(nums) == 1:
            if nums[0] == 1:
                return 0
            else:
                return 1

        nums.sort()

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return i + 1