from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        heap = []

        for char, freq in count.items():
            heapq.heappush(heap, (-freq, char))

        result = []

        prev_freq = 0
        prev_char = ""

        while heap:
            freq, char = heapq.heappop(heap)

            result.append(char)

            # Put the previous character back into the heap
            # if it still has copies left.
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            freq += 1

            prev_freq = freq
            prev_char = char

        if len(result) != len(s):
            return ""

        return "".join(result)