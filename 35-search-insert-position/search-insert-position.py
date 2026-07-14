class Solution(object):
    def searchInsert(self, nums, target):
        for x in range(len(nums)):
            print (x)
            if nums[x]== target:
                return x
            elif (nums[x]>target and nums[x-1]<target):
                return x
            elif (nums[x]>target):
                return x
        print (len(nums))
        print (x)
        if len(nums)==1 and target<nums[0]:
            return 0
        elif (nums[x]<target):
            return x+1