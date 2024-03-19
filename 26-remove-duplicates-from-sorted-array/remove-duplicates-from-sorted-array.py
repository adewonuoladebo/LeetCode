class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 1 #there is at least one unique number in the list
        
        #Unique is like a counter that stays on the first duplicate
        #say we have removeDuplicates([0,0,1,1,1,2,2,3,3,4]), we know there's at least one unique number (the first number - 0)
        #because nums[1] which is 0 equals nums[0], the list stays the same and nothing happens to unique
        #because nums[2] which is 1 doesn't equal nums[1] which is 0, nums[unique = 1] changes to the value of nums[i=2]
        #Unique count increases by 1 taking into account the appearance of another unique number


        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:   
                nums[unique] = nums[i]
                unique += 1 #every time a number isn't equal to the previous number, we have a new unique number
            
        return unique
        

      