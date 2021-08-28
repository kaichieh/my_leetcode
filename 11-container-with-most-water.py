from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_v = 0
        i = 0
        j = len(height) -1
        while(j>=i):
            v = self.getV(i, j, height)
            if v > max_v:
                max_v = v
            if height[j] > height[i]:
                i = i+1
            else:
                j = j-1
        return max_v
    
    def getV(self, i, j , height):
        lower = height[j] if height[i]> height[j] else  height[i]
        return lower * (j-i)
