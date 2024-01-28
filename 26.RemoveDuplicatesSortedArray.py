class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr=0
        for i in range(len(nums)):
            if nums[ptr]!=nums[i]:
                nums[ptr+1]=nums[i]
                ptr+=1
        return (ptr+1)
               