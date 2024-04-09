class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        to_replace = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[to_replace] = nums[i]
                to_replace += 1

        return to_replace