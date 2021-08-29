class Solution:
    def isValid(self, s: str) -> bool:
        history = []
        parMap = {')':'(', ']':'[', '}':'{'}
        for char in s:
            last = history[-1] if len(history) !=0 else None
            if char in ['(', '[', '{']:
                history.append(char)
            elif parMap[char] is last:
                history.pop()
            else:
                return False
        if len(history):
            return False
        return True
