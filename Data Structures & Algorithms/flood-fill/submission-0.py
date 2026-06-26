class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        row = len(image)
        col = len(image[0])
        original = image[sr][sc]
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if 0 <= sr < row and 0 <= sc < col:
            image[sr][sc] = color
            for direction in dirs:
                newR = sr + direction[0]
                newC = sc + direction[1]
                if 0 <= newR < row and 0 <= newC < col and image[newR][newC] == original:
                    self.floodFill(image, newR, newC, color)
        return image