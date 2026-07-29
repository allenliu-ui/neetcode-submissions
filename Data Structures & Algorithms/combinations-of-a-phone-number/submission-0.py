class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        combs = []
        self.helper(nums, 0, [], combs, digits)
        return combs
    
    def helper(self, nums, i, currCombs, combs, digits):
        if not digits:
            return []
        if len(currCombs) == len(digits):
            combs.append("".join(currCombs))
            return
        if i >= len(digits) or len(currCombs) > len(digits):
            return
        for char in nums[int(digits[i])]:
            currCombs.append(char)
            self.helper(nums, i + 1, currCombs, combs, digits)
            currCombs.pop()
