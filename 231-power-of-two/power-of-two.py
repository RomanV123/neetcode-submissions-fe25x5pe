class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #precheck 

        if n == 0:
            return False

        while n > 0 or n < 0:
        
            if n == 1:
                return True

        
            if n % 2 == 1:
                return False
    
            while n % 2 == 0:
                n = n // 2
        return True
        