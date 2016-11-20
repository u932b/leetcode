class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #  n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
        # Compared to linked-lists, with an array we have the total count, index of the array at our disposal

        # This attempt try to do it in place, moving from the initial index to the one just being replaced, with O(1) additional space
        # Unfortunately this does not work as we might get caught in loop such as (0+4)%4 = 0
        array_length = len(nums)
        count = 0
        i = 0
        to_replace = nums[0]
        while count < array_length:
            replace_index = (i + k) % array_length
            tmp = nums[replace_index]
            nums[replace_index] = to_replace
            i = replace_index
            to_replace = tmp
            count += 1
