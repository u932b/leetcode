class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #  n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
        # Compared to linked-lists, with an array we have the total count, index of the array at our disposal
        array_length = len(nums)
        separating_index = array_length - (k % array_length)
        nums = nums[separating_index:] + nums[:separating_index]
        return nums
