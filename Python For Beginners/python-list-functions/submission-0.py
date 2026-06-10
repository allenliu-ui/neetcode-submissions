from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum = 0
    for num in nums:
        sum += num
    return sum

def get_min(nums: List[int]) -> int:
    minNum = nums[0]
    for num in nums:
        minNum = min(minNum, num)
    return minNum

def get_max(nums: List[int]) -> int:
    maxNum = nums[0]
    for num in nums:
        maxNum = max(maxNum, num)
    return maxNum
# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
