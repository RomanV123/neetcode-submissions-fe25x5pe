class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        count1 = {}
        for char in s:
            count[char] = count.get(char,0) + 1
        
        for char in t:
                count1[char] = count1.get(char, 0) + 1
        if count1 == count:
            return True
        else:
            return False
        