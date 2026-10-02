class Solution:

    def plusOne(self, digits: list[int]) -> list[int]:
        # 1. If the last digit is a 9, it needs to carry over
        # We loop backward through the list
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0  # 9 becomes 0, and we move to the next digit left
            else:
                # 2. If it's NOT a 9, we can safely use your logic!
                digits[i] += 1
                return digits  # We are done, return the modified array

        # 3. Edge case: If the loop finishes, it means ALL digits were 9s (e.g., )
        # We need to add a 1 at the very beginning (e.g., )
        return [1] + digits
