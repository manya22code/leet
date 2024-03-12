class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=0
        b=True
        for i in range(len(s)):
            a=t.find(s[i],a,len(t))
            a=a+1
            print(a)
            if a==0:
                return False
            elif a>len(t):
                return False
            else:
                b= True
        return b