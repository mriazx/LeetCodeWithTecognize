class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s=0
        e=len(nums)-1
        while s<=e:
            if nums[s]==val:
                nums[e], nums[s] = nums[s], nums[e]
                e-=1
            else:
                s+=1
        return s