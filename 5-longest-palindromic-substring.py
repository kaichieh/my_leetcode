class Solution:
    def longestPalindrome(self, s: str) -> str:
        new_str = insert(s)
        new_r = []
        center = 0
        R = 0
        
        for i in range(len(new_str)):
            new_r.append(1)
            if i <= ( center + R ):
                new_r[i] = min( new_r[2*center - i], R - (i-center) +1)
                j = i + new_r[i] -1
                k = i - new_r[i] +1
            else:
                new_r[i] = 1
                j=i
                k=i
            
            while( (j+1) <len(new_str) and (k-1) >=0 and new_str[j+1] == new_str[k-1]):
                new_r[i]+=1
                j+=1
                k-=1
            
            if new_r[i] > new_r[center] or ( new_r[i] == new_r[center] and (i %2==1)):
                center = i
                R = new_r[i]-1
                
        result =  new_str[center-R:center+R+1]
        if result is "-":
            return s[0]
        else:
            return result.replace("-", "")
    

def insert(s):
    length = len(s) -1
    while(length !=0):
        s = s[:length] + "-" + s[length:]
        length -=1
    return s
