class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ""
        min_length = min(len(word1), len(word2))
        leftover = word1[min_length:] or word2[min_length:]
        for x, y in zip(word1, word2):
            final += x + y
        return final + leftover

# Time complexity: O(n) where n is the length of the longer string
# Space complexity: O(n)
