class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c for c in s if c.isalnum())
        return cleaned.lower() == cleaned[::-1].lower()

# Time complexity: O(n)
# Space complexity: O(n)
# [::-1] reverses the string using slice notation [start:stop:step]
