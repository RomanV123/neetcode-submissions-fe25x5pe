class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # Loop through indices sequentially (0, 1, 2...)
        for i in range(len(nums)):
            
            # Isolate the current number to calculate its digit sum
            number = nums[i]
            digit_sum = 0
            
            # Peel off digits one by one until the number is 0
            while number > 0:
                digit_sum += number % 10
                number = number // 10
                
            # Special case: if the original number was 0, its sum is 0
            if nums[i] == 0:
                digit_sum = 0
                
            # Because we go left-to-right, the FIRST match is the smallest index
            if digit_sum == i:
                return i
                
        # If the loop finishes and no index matched, return -1
        return -1
