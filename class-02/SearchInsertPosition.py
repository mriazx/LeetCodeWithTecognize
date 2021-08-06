class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s=0
        e=len(nums)-1
        while s<=e:
            if target <= nums[s]:
                return s
            elif target >nums[e]:
                return len(nums)
            else:
                s+=1