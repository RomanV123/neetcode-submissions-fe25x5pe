import math

class Solution:
    def mySqrt(self, x: int) -> int:
        count = 0
        while count*count <=x:
            count+=1

        else:
            return count -1

            