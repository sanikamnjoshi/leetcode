class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # lower complexity
        for idx1 in range(len(nums)):
            for idx2 in range(idx1 + 1, len(nums)):
                if nums[idx1] + nums[idx2] == target:
                    return [idx1, idx2]

        return None

        # higher complexity (O(n^2))
        #for idx1, num1 in enumerate(nums):
        #    for idx2, num2 in enumerate(nums):
        #        if idx1 == idx2:
        #            pass
        #        else:
        #            if (num1 + num2) == target:
        #                return[idx1, idx2]
        #            else:
        #                pass
        #
        #return None
