class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        n=a[-1]
        count=len(n)
        return count