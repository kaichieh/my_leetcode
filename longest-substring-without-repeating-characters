class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLengthPerChar = {}
        maxLength = 0
        firstIndex = 0
        index = 0
        for char in s:
            if char in maxLengthPerChar:
                if maxLengthPerChar[char] +1 > firstIndex:
                    firstIndex = maxLengthPerChar[char] +1
            maxLengthPerChar[char] = index
            newLength = index - firstIndex +1
            if newLength > maxLength:
                maxLength = newLength
            index +=1
        return maxLength
