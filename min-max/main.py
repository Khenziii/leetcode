class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return nums[0]

        newNums = [1 for _ in range(int(n / 2))]

        for i in range(len(newNums)):
            if(i % 2 == 0):
                if(0 <= i < n / 2):
                    newNums[i] = min(nums[2 * i], nums[2 * i + 1])
            elif(i % 2 != 0):
                if(0 <= i < n / 2):
                    newNums[i] = max(nums[2 * i], nums[2 * i + 1])
        
        return self.minMaxGame(newNums)

