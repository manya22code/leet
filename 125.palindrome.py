class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=""
        left=0
        right=-1
        
        for i in range(len(s)):
            if s[i].isalnum():
                a+=s[i]
                                      
        if a=="" or a==" ":
             return True                         
                                      
                                      
        for b in range(len(a)):
            if a[left]==a[right]:
                left+=1
                right-=1
                if left>=len(a):
                    return True
                
                    
            else:
                return False
            