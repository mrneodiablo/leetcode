class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = sorted(nums)
        max = 0
        for i in range(0, len(tmp)/2):
            a = tmp[i] + tmp[len(tmp)-i-1]
            if a > max:
                max = a
        return max
