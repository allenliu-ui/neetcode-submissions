class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        while numRows > 1:
            newAdd = [1]
            for i in range(len(res[-1]) - 1):
                newAdd.append(res[-1][i] + res[-1][i + 1])
            newAdd.append(1)
            res.append(newAdd)
            numRows -= 1
        return res
