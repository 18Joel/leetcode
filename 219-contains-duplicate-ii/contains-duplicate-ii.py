class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        a=set()
        for i in range(len(nums)):
            if i>k:
                a.remove(nums[i-k-1])
            if nums[i] in a:
                return True
            a.add(nums[i])
        return False