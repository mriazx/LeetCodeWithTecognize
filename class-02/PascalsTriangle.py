class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        result=[[1],[1,1]]
        for i in range(2,numRows):
            temp = [1,1]
            for j in range(1, i):
                temp.insert(-1, (result[-1][j-1]+result[-1][j]))
            result.append(temp)
        return result