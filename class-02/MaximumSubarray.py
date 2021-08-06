class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # using kadane's algorithm.
        temp = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            temp = temp+nums[i]
            if temp<nums[i]:
                temp=nums[i]
            if total < temp:
                total = temp
        return total