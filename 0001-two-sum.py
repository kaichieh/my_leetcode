from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history_num = {}
        index = 0
        for num in nums:
            if (target - num) in history_num:
                return [history_num[target - num], index]
            else:
                history_num[num] = index
                index +=1
        return []
