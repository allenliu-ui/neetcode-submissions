class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if (matrix[mid][-1] < target):
                left = mid + 1
            elif (matrix[mid][0] > target):
                right = mid - 1
            else:
                return self.binary(matrix[mid], 0, len(matrix[mid]), target)
        return False


    def binary(self, arr, left, right, target):
        if left > right:
            return False
        mid = (left + right) // 2
        if arr[mid] < target:
            return self.binary(arr, mid + 1, right, target)
        elif arr[mid] > target:
            return self.binary(arr, left, mid - 1,  target)
        else:
            return True