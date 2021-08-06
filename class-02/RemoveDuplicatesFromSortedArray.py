class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
        while s<len(nums)-1:
            if nums[s]!=nums[s+1]:
                s+=1
            else:
                nums.remove(nums[s])