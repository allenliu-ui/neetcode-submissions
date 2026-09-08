class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        def circle (top, down, left, right, res):
            if top >= down or left >= right:
                return
            rightMove = left 
            downMove = top + 1
            leftMove = right - 2
            upMove = down - 2
            while rightMove < right:
                res.append(matrix[top][rightMove])
                rightMove += 1
            if top + 1 < down:
                while downMove < down:
                    res.append(matrix[downMove][right - 1])
                    downMove += 1
            if left < right - 1 and top + 1 < down:
                while leftMove > left:
                    res.append(matrix[down - 1][leftMove])
                    leftMove -= 1
                upMove = down - 1
                while upMove > top:
                    res.append(matrix[upMove][left])
                    upMove -= 1
            top += 1
            down -= 1
            left += 1
            right -= 1
            circle(top, down, left, right, res)
        circle(0, len(matrix), 0, len(matrix[0]), res)
        return res