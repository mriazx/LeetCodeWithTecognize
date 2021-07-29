# Runtime: 112 ms, beats 42.04 % of python3 submissions.
# Memory Usage: 14.9 MB, beats 80.58 % of python3 submissions.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = len(nums)-1
        e = 0
        while s>=e:
            x = target-nums[s]
            if x not in nums[:s]:
                s-=1
            else:
                return nums.index(x, 0, s), s
