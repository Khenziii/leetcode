class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums: List[int] = nums1 + nums2
        nums = sorted(nums)

        if len(nums) % 2 == 0:
            middle_indexes = [len(nums) / 2, len(nums) / 2 + 1]
            middle_values = [nums[int(i) - 1] for i in middle_indexes]

            average = sum(middle_values) / 2
            median = average
        else:
            middle_index = int(len(nums) / 2)
            median = nums[middle_index]
        
        return median

