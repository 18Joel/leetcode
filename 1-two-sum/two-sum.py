class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for x in range(n):         
            r = target - nums[x]          
            if r in nums:
                i = nums.index(r)
                if x != i:
                    return (x,i)
