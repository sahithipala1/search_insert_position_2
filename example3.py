from typing import List


def findIndex(self, nums: List[int],n,  target: int) -> int:
    for i in range(n):
        if nums[i] == target:
            return i
        if nums[i] > target:
            return i
    
    return n


nums = [1, 2, 3, 4, 5]
n = len(nums)
target = 6
print(findIndex(nums,n, target = target))
