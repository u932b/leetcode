from Inputs import Inputs


class Solution(object):

    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        array_length = len(nums)
        separating_index = array_length - (k % array_length)
        # nums[:] change the value of old nums, but nums just changes
        # its reference to a new nums not the value of old nums
        nums[:] = nums[separating_index:] + nums[:separating_index]
        # Alternatively
        # nums[:] = nums[-(k % array_length):] + nums[:-(k % array_length)]

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # n = 7 and k = 3, the array [1,2,3,4,5,6,7]
        # is rotated to [5,6,7,1,2,3,4].
        # Compared to linked-lists, with an array we have the total count,
        # index of the array at our disposal

        # This is a smart solution that only utilize O(1) space when
        # creating tmp in def reverse
        n = len(nums)
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1

if __name__ == "__main__":
    input_data = [1, 2, 3, 4, 5, 6, 7]
    inp = Inputs(input_data, 'array')
    input_result = inp.returnResult()

    sol = Solution()
    print input_data
    sol.rotate1(input_data, 3)
    print input_data
