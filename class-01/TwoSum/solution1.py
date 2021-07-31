# Runtime: 52 ms, beats 96.56 % of python3 submissions.
# Memory Usage: 15.4 MB, beats 20.52 % of python3 submissions.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        s = 0
        e = len(nums)-1
        while s<=e:
            x = target-nums[s]
            if x in d:
                return [d[x], s]
            d[nums[s]] = s
            s+=1
