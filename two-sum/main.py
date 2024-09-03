class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            needed_num = target - nums[i]
            if(needed_num in nums):
                if(nums.index(nums[i]) == nums.index(needed_num)):
                    try:
                        if(nums.index(nums[i]) > nums[nums.index(needed_num) + 1:].index(needed_num) + nums.index(needed_num) + 1):
                            return [nums.index(needed_num), nums[nums.index(needed_num) + 1:].index(needed_num) + nums.index(needed_num) + 1]
                        else:
                            return [nums.index(nums[i]), nums[nums.index(needed_num) + 1:].index(needed_num) + nums.index(needed_num) + 1]
                    except:
                        continue

                if(nums.index(nums[i]) > nums.index(needed_num)):
                    return [nums.index(needed_num), nums.index(nums[i])]
                else:
                    return [nums.index(nums[i]), nums.index(needed_num)]

