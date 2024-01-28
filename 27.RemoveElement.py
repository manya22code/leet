class Solution(object):
    def removeElement(self, nums, val):
        j=0
        count=len(nums)

        for i in range(count):
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1   
        return j  