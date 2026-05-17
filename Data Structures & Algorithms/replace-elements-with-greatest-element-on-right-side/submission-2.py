class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0, len(arr)):
            max = -1
            for j in range(i+1, len(arr)):
                if (arr[j] > max):
                    max = arr[j]
            arr[i] = max
        return arr    