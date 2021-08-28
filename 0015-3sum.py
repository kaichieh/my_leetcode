from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        result = set()
        for index, value in enumerate(nums[:-2]):
            if index >0 and value == nums[index-1]:
                continue
            d = {}
            for x in nums[index+1:]:
                if x not in d:
                    d[-value-x] = 1
                else:
                    result.add((value, -value-x, x))
        return list(result)
