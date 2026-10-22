class Solution:
    def toHex(self, num: int) -> str:
        hex_chars = "0123456789abcdef"
        remainders = []
        
        if num == 0:
            return "0"
        
        if num < 0:
            num = num + 2**32
        
        while num > 0:
            quotient = num // 16 
            remainder = num % 16
            remainders.append(remainder)
            
            num = quotient

        converted_chars = [hex_chars[r] for r in remainders]
        
        return "".join(reversed(converted_chars))

        

        