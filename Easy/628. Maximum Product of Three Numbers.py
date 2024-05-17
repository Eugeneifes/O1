class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]

        nums = sorted(nums)

        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])