class Solution:
    def reverseDegree(self, s: str) -> int:

        total = 0 
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        alphabet_dict = {
            char:26 - i
            for i, char in enumerate(alphabet)

        }
        
        for position, letter in enumerate(s, start = 1):
            reverse_index = alphabet_dict[letter]

            product = position*reverse_index
            total += product


        return total