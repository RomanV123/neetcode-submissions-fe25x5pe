class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in range(len(s)):
            word = s.split()
            last_word = word[-1]

            last_word_count = len(last_word)

            return last_word_count

        