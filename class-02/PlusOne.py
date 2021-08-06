class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        t = str(int("".join(s))+1)
        return [int(i) for i in t]